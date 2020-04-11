#!/usr/bin/env python3

import binascii, json
from Crypto.PublicKey import RSA

class wallet:
    file_name = 'wallet.json'

    def __init__(self):
        self.balance = 0
        self.private_key = ''
        self.public_key = ''
        try:
            wallet_file = open(self.file_name)
            data = json.loads(wallet_file.read())
            self.balance = data['balance']
            self.private_key = data['private_key']
            self.public_key = data['public_key']
        except FileNotFoundError:
            pass
    
    def generate(self):
        key = RSA.generate(1024)
        self.balance = 0
        self.private_key = binascii.hexlify(key.exportKey(format='DER')).decode('ascii')
        self.public_key =  binascii.hexlify(key.publickey().exportKey(format='DER')).decode('ascii')
        self.save()
    
    def save(self):
        json_string = json.dumps(
            {'balance': self.balance, 'private_key': self.private_key, 'public_key': self.public_key},
            indent=4
        )
        wallet_file = open(self.file_name, 'w')
        wallet_file.write(json_string)
        wallet_file.close()