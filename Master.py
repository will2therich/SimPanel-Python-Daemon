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

