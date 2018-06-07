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
# ________________________________________________________________________________________________________________________
#                       DO NOT EDIT
#
from Authenticator import authenticate

authorisedClients = []

# Handles all the commands and sends them to the right place!
def handlecommand(command, data, client):
    print("Handling Command", command)

    if command == 'authenticate':
        authenticated = authenticate(data, client)
        if authenticated:
            authorisedClients.append(client)
            message = "Access Granted"
            return message
        else:
            message = "Access Denied"
            return message

    if command == 'ping':
        return 'pong'

    if command == 'close':
        authorisedClients.remove(client)
        return 'close'

