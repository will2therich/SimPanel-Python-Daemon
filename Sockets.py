from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket, SimpleSSLWebSocketServer
from Master import handlecommand

clients = []


class DaemonWebsocketService(WebSocket):

    def handleConnected(self):
        print(self.address, 'connected')
        clients.append(self)
        for client in clients:
            client.sendMessage(self.address[0] + u' - connected')

    def handleClosed(self):
        print(self.address, 'closed')
        clients.remove(self)
        for client in clients:
            client.sendMessage(self.address[0] + u' - disconnected')

    def handleMessage(self):
        print(self.address, self.data)

        if ':' in self.data:
            data = self.data
            seperatedData = data.split(':')
            returnMessage = handlecommand(seperatedData[0], seperatedData[1], self)

            self.sendMessage(u'Returned:' +returnMessage)


# server = SimpleWebSocketServer('', 9005, DaemonWebsocketService)
server = SimpleSSLWebSocketServer('', 9005, DaemonWebsocketService, './ssl-cert-snakeoil.pem',
                                  './ssl-cert-snakeoil.key')

server.serveforever()
