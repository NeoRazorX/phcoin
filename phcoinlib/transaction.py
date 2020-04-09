#!/usr/bin/env python3

class transaction:
    def __init__(self, senderWallet, address, amount):
        self.senderAddr = senderWallet.publicKey
        self.recipientAddr = address
        self.amount = amount