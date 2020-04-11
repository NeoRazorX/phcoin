#!/usr/bin/env python3

import json
from .block import block

class blockchain:
    file_name = 'blockchain.json'

    def __init__(self):
        self.blocks = []
        self.last_hash = None
        self.last_number = 0
        try:
            blockchain_file = open(self.file_name)
            data = json.loads(blockchain_file.read())
            for item in data['blocks']:
                self.load(item)
        except FileNotFoundError:
            pass
    
    def __str__(self):
        blocks = []
        for item in self.blocks:
            blocks.append(item.to_dict())
        return json.dumps({'blocks': blocks}, indent=4)
    
    def add(self, new_block):
        self.blocks.append(new_block)
        self.last_hash = new_block.hash
        self.last_number = new_block.number
        self.save()
    
    def balance(self, address):
        balance = 0
        for item in self.blocks:
            if item.miner == address:
                balance += item.reward
        return balance
    
    def last(self):
        return self.blocks[-1]
    
    def load(self, item):
        new_block = block(item['transactions'], item['number'], item['last_hash'])
        new_block.hash = item['hash']
        new_block.miner = item['miner']
        new_block.reward = item['reward']
        new_block.timestamp = item['timestamp']
        if self.validate(new_block):
            self.blocks.append(new_block)
            self.last_hash = new_block.hash
            self.last_number = new_block.number
        else:
            print('invalid block: ' + str(new_block.number))

    def mine(self, miner):
        new_block = block([], 1 + self.last_number, self.last_hash)
        new_block.miner = miner
        new_block.reward = 100
        new_block.hash = new_block.get_hash()
        self.add(new_block)
    
    def save(self):
        blockchain_file = open(self.file_name, 'w')
        blockchain_file.write(str(self))
        blockchain_file.close()
    
    def validate(self, new_block):
        if new_block.last_hash != self.last_hash:
            return False
        elif new_block.hash != new_block.get_hash():
            return False
        else:
            return True