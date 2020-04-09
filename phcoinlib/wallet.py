#!/usr/bin/env python3

import binascii, json
from Crypto import Random
from Crypto.PublicKey import RSA

class wallet:
    fileName = 'phcoin.cfg'
    privateKey = ''
    publicKey = ''

    def __init__(self):
        try:
            configFile = open(self.fileName)
            data = json.loads(configFile.read())
            self.privateKey = data['privateKey']
            self.publicKey = data['publicKey']
        except FileNotFoundError:
            pass
    
    def generate(self):
        key = RSA.generate(1024, Random.new().read)
        self.privateKey = binascii.hexlify(key.exportKey(format='DER')).decode('ascii')
        self.publicKey =  binascii.hexlify(key.publickey().exportKey(format='DER')).decode('ascii')
        self.save()
    
    def save(self):
        jsonString = json.dumps({'privateKey': self.privateKey, 'publicKey': self.publicKey})
        configFile = open('phcoin.cfg', 'w')
        configFile.write(jsonString)
        configFile.close()