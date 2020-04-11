#!/usr/bin/env python3

import datetime, hashlib, json

class block:
    def __init__(self, transactions, number, last_hash):
        self.hash = None
        self.last_hash = last_hash
        self.miner = None
        self.number = number
        self.reward = 0
        self.timestamp = datetime.datetime.utcnow()
        self.transactions = transactions
    
    def __str__(self):
        return json.dumps({
            'hash': self.hash,
            'last_hash': self.last_hash,
            'miner': self.miner,
            'number': self.number,
            'reward': self.reward,
            'timestamp': self.timestamp.__str__(),
            'transactions': self.transactions
        })
    
    def build(self):
        json_string = json.dumps({
            'last_hash': self.last_hash,
            'miner': self.miner,
            'number': self.number,
            'reward': self.reward,
            'timestamp': self.timestamp.__str__(),
            'transactions': self.transactions
        })
        self.hash = hashlib.sha256(json_string.encode('utf-8')).hexdigest()