#!/usr/bin/env python3

from Crypto import Random
from Crypto.PublicKey import RSA

class wallet:
    privateKey = None
    publicKey = None

    def generate(self):
        key = RSA.generate(2048)
        self.privateKey = key.exportKey('DER')
        self.publicKey =  key.publickey().exportKey('DER')