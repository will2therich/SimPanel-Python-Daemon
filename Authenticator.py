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
from config import *
import requests
import json


def authenticateKey(key):
    if key == authKey:
        if enviroment == 'dev':
            print("Authenticator called.")
            # Due to it being a dev enviroment SSL certificates are not checked. DO NOT USE DEV IN A PRODUCTION ENVIRONMENT
            r = requests.post('https://simpanel.local/daemon/verify', data={'daemonKey': key} , verify=False)
            print(r.status_code, r.reason)
            data = r.json()
            return data
        else:
            r = requests.post('https://simpanel.local/daemon/verify', data={'daemonKey': key})
            data = r.json()
            return data

def authenticate(data, client):

    siteConfirmation = authenticateKey(data)
    pythonData = json.loads(siteConfirmation)
    authorised = pythonData['authorised']

    print(authorised)

    if authorised == 'yes':
        if enviroment == 'dev':
            print('Connection Accepted', client.address)
        return True

    if enviroment == 'dev':
        print('Connection Rejected', client.address)
    return False
