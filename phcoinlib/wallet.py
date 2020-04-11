#!/usr/bin/env python3

import binascii, json
from Crypto import Random
from Crypto.PublicKey import RSA

class wallet:
    file_name = 'phcoin.cfg'

    def __init__(self):
        try:
            config_file = open(self.file_name)
            data = json.loads(config_file.read())
            self.private_key = data['private_key']
            self.public_key = data['public_key']
        except FileNotFoundError:
            self.private_key = ''
            self.public_key = ''
    
    def generate(self):
        key = RSA.generate(1024, Random.new().read)
        self.private_key = binascii.hexlify(key.exportKey(format='DER')).decode('ascii')
        self.public_key =  binascii.hexlify(key.publickey().exportKey(format='DER')).decode('ascii')
        self.save()
    
    def save(self):
        json_string = json.dumps({'private_key': self.private_key, 'public_key': self.public_key})
        config_file = open('phcoin.cfg', 'w')
        config_file.write(json_string)
        config_file.close()