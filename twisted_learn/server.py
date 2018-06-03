from twisted.internet.protocol import Protocol, Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor

clients = []


class Spreader(Protocol):
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.numProtocols += 1
        self.transport.write('欢迎来到Spreader Site，你是第%s个客户端用户！\n' % self.factory.numProtocols)
        print('new connect: %d' % self.factory.numProtocols)
        clients.append(self)

    def connectionLost(self, reason):
        self.factory.numProtocols -= 1
        clients.remove(self)
        print('lost connect: %d' % self.factory.numProtocols)

    def dataReceived(self, data):
        if data == 'close':
            self.transport.loseConnection()
            for client in clients:
                if client != self:
                    client.transport.write(data)
        else:
            print(data)


class SpreadFactory(Factory):
    def __init__(self):
        self.numProtocols = 0

    def buildProtocol(self, addr):
        return Spreader(self)


endpoint = TCP4ServerEndpoint(reactor, 8007)
endpoint.listen(SpreadFactory())
reactor.run()
