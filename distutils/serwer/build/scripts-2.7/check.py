from twisted.internet.protocol import ClientFactory, Protocol
from twisted.internet import reactor
import sys

class CP(Protocol):
    
    def connectionMade(self):
        print 'connection'
        self.transport.write('c')
    
    def dataReceived(self, data):
        print data
        
    def connectionLost(self, reason):
        print "connection lost"
        
class CF(ClientFactory):
    protocol = CP
    
    def __init__(self):
        pass
    
    def clientConnectionFailed(self, connector, reason):
        print "Connection failed - goodbye!"
        reactor.stop()
    
    def clientConnectionLost(self, connector, reason):
        print "Connection lost - goodbye!"
        reactor.stop()


reactor.connectTCP('localhost',8000, CF())
reactor.run()