#   _________.__                                   .__
#  /   _____/|__| _____ ___________    ____   ____ |  |
#  \_____  \ |  |/     \\____ \__  \  /    \_/ __ \|  |
#  /        \|  |  Y Y  \  |_> > __ \|   |  \  ___/|  |__
# /_______  /|__|__|_|  /   __(____  /___|  /\___  >____/
#         \/          \/|__|       \/     \/     \/
# ________
# \______ \ _____    ____   _____   ____   ____
#  |    |  \\__  \ _/ __ \ /     \ /  _ \ /    \
#  |    `   \/ __ \\  ___/|  Y Y  (  <_> )   |  \
# /_______  (____  /\___  >__|_|  /\____/|___|  /
#         \/     \/     \/      \/            \/
#
#________________________________________________________________________________________________________________________
#                       DO NOT EDIT
#
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket, SimpleSSLWebSocketServer
from Master import handlecommand
from config import *

clients = []


class DaemonWebsocketService(WebSocket):

    def handleConnected(self):
        print(self.address, 'connected')
        clients.append(self)
        for client in clients:
            client.sendMessage(self.address[0] + u' - connected')

    def handleClosed(self):
        clients.remove(self)
        for client in clients:
            client.sendMessage(self.address[0] + u' - disconnected')

    def handleMessage(self):
        print(self.address, self.data)

        if ':' in self.data:
            data = self.data
            seperatedData = data.split(':')
            returnMessage = handlecommand(seperatedData[0], seperatedData[1], self)

            # Handling closing via command
            if returnMessage == 'close':
                print(self.address , "Disconnected")
                self.sendMessage(u'Returned:' + returnMessage)
                self.handleClosed(self)

            self.sendMessage(u'Returned:' +returnMessage)


# Update the certificate files in the config
# In order to use SSL you'll need to link the ip to a domain and SSL the domain.
if sslEnable:
    server = SimpleSSLWebSocketServer(ipToListenOn, portToListenOn, DaemonWebsocketService, sslCert,  sslKey)
    print("Websockets Live and listening on port: " + str(portToListenOn))
else:
    server = SimpleWebSocketServer(ipToListenOn, portToListenOn, DaemonWebsocketService)
    print("Websockets Live and listening on port: " + str(portToListenOn))

server.serveforever()
