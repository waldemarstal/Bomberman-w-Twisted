import socket, pygame,cPickle,sys,os,select,time
from protocolObjects import *
from pygame.locals import * 
from twisted.internet.protocol import Protocol, ClientFactory
clock = pygame.time.Clock()

class CP(Protocol):
	def __init__(self):
		None
		
	def connectionMade(self):
		self.factory.SConnectionMade(self)

	def dataReceived(self, data):
		data = cPickle.loads(data)
		clock.tick(20)
		if isinstance(data,Countdown):
			if data.number == 3:
				self.factory.Run(data)
			self.factory.RunC(data)	
			pygame.display.update()	
		elif isinstance(data, Map):
			self.factory.Update(data)
			self.factory.Send()
			pygame.display.update()
		elif isinstance(data, Result):
			self.factory.CFResult(data)
		else:
			print data
			
	def connectionLost(self, reason):
		pygame.quit()
		self.go = False
		reactor.callLater(5,reactor.stop)
	
class CF(ClientFactory):
	protocol = CP

	def __init__(self):
		pass

	def SConnectionMade(self,s):
		self.server = s

	def Run(self,data):
		self.run = Game(data.mapSize,data.playerId)
		self.run.initGame(data)
		
	def RunC(self, data):
		self.run.Count(data)

	def Update(self,data):
		self.run.UpdateScr(data)

	def Send(self):
		a = self.run.Akcja()
		b = cPickle.dumps(a)
		self.server.transport.write(b)
	
	def CFResult(self,data):
		self.run.PR(data)
		
class Game(object):
	def __init__(self,mapSize,playerId):
		pygame.init()
	def PR(self,data):
		tekst = self.font.render('Koniec',True, (30,100,200))
		tekst2 = self.font.render('Wygral gracz: ' + str(data.winners + 1), True, (0,0,0))
		tekst3 = self.font.render('Wynik: ' + str(data.scores), True, (0,0,0))
		self.screen.fill((250,250,250))
		self.screen.blit(tekst,(50,50))
		self.screen.blit(tekst2,(50,200))
		self.screen.blit(tekst3,(50,300))
		pygame.display.update()
		time.sleep(5)
		pygame.quit()
		
	def Count(self, data):
		tekst = self.font.render(str(data.number),True, (0,0,0))
		self.screen.fill((250,250,250))
		self.screen.blit(tekst, (300,200))
		
	def Draw(self,scr,i,pos):
		i += 1
		obr = 'gr' + str(i) + '.png'
		os = pygame.image.load(obr).convert_alpha()
		scr.blit(os, pos)
		   

	def initGame(self,data):
		pygame.init()
		self.screen = pygame.display.set_mode((data.mapSize[0], data.mapSize[1]))
		self.ID = data.playerId
		pygame.display.set_caption("Gracz " + str(self.ID + 1))
		self.font = pygame.font.Font("CatShop.ttf", 72)
		self.warstwa = pygame.image.load('plik.jpg').convert_alpha()
		self.b = pygame.image.load('mina.png').convert_alpha()

	def UpdateScr(self, data):
		self.warstwa = pygame.image.load('plik.jpg').convert_alpha()
		self.b = pygame.image.load('mina.png').convert_alpha()
		for i in data.mines:
			self.warstwa.blit(self.b, i.position)
		for i, pos in enumerate( data.playersPositions ):
			self.Draw(self.warstwa,i,(pos.x,pos.y))
		self.screen.blit(self.warstwa, (0,0))

	def Akcja(self):
		pressed_keys = pygame.key.get_pressed()
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()

		if pressed_keys[K_LEFT]:
			PlayerAction.action = 'left'
		elif pressed_keys[K_RIGHT] :
			PlayerAction.action = 'right'
		elif pressed_keys[K_UP]:
			PlayerAction.action = 'up'
		elif pressed_keys[K_DOWN]:
			PlayerAction.action = 'down'
		elif pressed_keys[K_LCTRL]:
			PlayerAction.action = 'result'
		elif pressed_keys[K_SPACE]:
			PlayerAction.action = 'bomb'
		else:
			PlayerAction.action = 'none'

		return PlayerAction.action


from twisted.internet import reactor
reactor.connectTCP('localhost',8001, CF())
reactor.run()