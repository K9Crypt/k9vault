import hashlib
from src.encrypt import k9signature

def saveKey(key):
    with open('secret.key', 'wb') as key_file:
        key_file.write(key)

def loadKey():
    with open('secret.key', 'rb') as key_file:
        return key_file.read()
