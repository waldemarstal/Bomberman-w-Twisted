from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor
from random import randint
import sys, cPickle, time
from protocolObjects import *
 
class Servprot(Protocol):
    def __init__(self, factory):
        self.factory = factory
 
    def connectionMade(self):
        self.factory.connectionMade(self)
 
    def dataReceived(self, data):
	data = cPickle.loads(data)
	a = self.factory.Akcja(self, data)
	b = cPickle.dumps(a)
	self.transport.write(b)
 
    def connectionLost(self, reason):
        self.factory.clients_remove(self)
 
class Fact(Factory):
    def __init__(self):
        self. gracze = {}
        self.player_id = 0
        Map.playersPositions = []
	Map.mines = []
	self.pkt = 0
	self.mapSize = 640,480
	self.odwiedzone = []
	self.odlicz = 0
	self.odl_wys = 3
        
    def ruch(self,y,x,ii):
		if (Position(y,x)) not in Map.playersPositions:
			Map.playersPositions[ii] = Position(y,x)
		for i in self.miny:
			if (x,y) == i.position:
			    Result.winners = (ii + 1) % 2
			    Result.scores = 'max'
			    self.m_end(Result.winners, Result.scores)

    def m_end(self,a,aa):
	for client in self.gracze:
	    b = cPickle.dumps(Result(a, aa))
	    client.transport.write(b)
	
	reactor.callLater(5,reactor.stop)
	
    def fun_res(self,x,y):
	    if (x, y) not in self.odwiedzone:
		    (self.odwiedzone).append((x, y))
		    if x >=0 and x<640 and y >= 0 and y < 480:
			    self.dod = True
			    for i in self.miny:
				    if (x, y) == i.position:
					    self.dod = False
			    if self.dod:
				    self.pkt += 1
				    self.fun_res(x - 40, y)
				    self.fun_res(x + 40, y)
				    self.fun_res(x, y - 40)
				    self.fun_res(x, y + 40)

    def buildProtocol(self, addr):
        return Servprot(self)
    
    def Akcja(self, idd , data):
	id = self.gracze[idd]
	x=(Map.playersPositions[id]).x
	y=(Map.playersPositions[id]).y
	if data == 'up':
		if y > 40:
			self.ruch(y-40,x,id)
			
	elif data == 'down':
		if y < 440:
			self.ruch(y+40,x,id)
			
	elif data == 'right':
		if x < 600:
			self.ruch(y,x+40,id)
			
	elif data == 'left':
		if x > 40:
			self.ruch(y,x-40,id)

	elif data == 'result':
		makss = (0,0)
		for client in self.gracze:
			self.pkt = 0
			self.odwiedzone = []
			xx = (Map.playersPositions[self.gracze[client]]).x
			yy = (Map.playersPositions[self.gracze[client]]).y
			self.fun_res(xx,yy)
			if makss[0] < self.pkt:
				makss = (self.pkt, self.gracze[client])
			elif makss[0] == self.pkt and makss[1] == id:
				makss = (self.pkt, self.gracze[client])
			self.odwiedzone = []
		Result.winners = makss[1]
		Result.scores = makss[0]
		self.m_end(Result.winners, Result.scores)
	
	elif data == 'none':
		pass
	    
	elif data == 'bomb':
		self.warunek = True
		if x%40 == 5 and y%40 == 5:
			for i in self.miny:
				if i.position == (x, y):
					self.warunek = False
			if self.warunek:
				bomba = Mine((x,y),id)
				Map.mines.append(bomba)
	self.miny= Map.mines
	a = Map(Map.mines,Map.playersPositions)
	return a
	
    def connectionMade(self,client):
	self.gracze[client] = self.player_id
	self.player_id += 1
	if self.player_id == 4:
	    reactor.callLater(1, self.countdown)
	    
    def countdown(self):
        for client in self.gracze:
            if self.odlicz == 3:
		obiekt = Map([],Map.playersPositions)
                m = cPickle.dumps(obiekt)
                for i in self.gracze:
                    i.transport.write(m)
                return
            else:
		if self.odlicz == 0:
		    ilosc = len(self.gracze)
		    id = self.gracze[client]
		    x = 5 + randint(id * (16/ilosc), (id + 1) * (16/ilosc)) * 40
		    y = 5 + randint(id * (12/ilosc), (id + 1) * (12/ilosc)) * 40
		    Map.playersPositions.append(Position(y,x))
                obiekt = cPickle.dumps(Countdown(self.odl_wys,self.mapSize,self.gracze[client]))
                client.transport.write(obiekt)
        self.odlicz += 1
	self.odl_wys -= 1
        reactor.callLater(1, self.countdown)
	
    def end(self,client):
	makss = (0,0)
	for client in self.gracze:
		self.pkt = 0
		self.odwiedzone = []
		xx = (Map.playersPositions[self.gracze[client]]).x
		yy = (Map.playersPositions[self.gracze[client]]).y
		self.fun_res(xx,yy)
		if makss[0] < self.pkt:
			makss = (self.pkt, self.gracze[client])
		elif makss[0] == self.pkt and makss[1] == id:
			makss = (self.pkt, self.gracze[client])
		self.odwiedzone = []
	Result.winners = makss[1]
	Result.scores = makss[0]
	return Result(Result.winners,Result.scores)
	
    def clients_remove(self,client):
        del self.gracze[client]

reactor.listenTCP(8001, Fact())
reactor.run()
