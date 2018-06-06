from config import *
import requests
import json


def authenticateKey(key):
    if key == authKey:
        if enviroment == 'dev':
            print("Authenticator called.")
            r = requests.post('https://simpanel.local/daemon/verify', data={'daemonKey': key} , verify=False)
            print(r.status_code, r.reason)
            data = r.json()
            return data
        else:
            r = requests.post('https://simpanel.local/daemon/verify', data={'daemonKey': key} , verify=False)
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
    else:
        if enviroment == 'dev':
            print('Connection Rejected', client.address)
        return False
