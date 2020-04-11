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
                new_block = block(item['transactions'], item['number'], item['last_hash'])
                new_block.hash = item['hash']
                new_block.miner = item['miner']
                new_block.reward = item['reward']
                new_block.timestamp = item['timestamp']
                self.blocks.append(new_block)
                self.last_hash = new_block.hash
                self.last_number = new_block.number
        except FileNotFoundError:
            pass
    
    def __str__(self):
        blocks = []
        for item in self.blocks:
            blocks.append(item.toDict())
        return json.dumps({'blocks': blocks}, indent=4)
    
    def add(self, new_block):
        self.blocks.append(new_block)
        self.last_hash = new_block.hash
        self.last_number = new_block.number
        self.save()
    
    def get_balance(self, address):
        balance = 0
        for item in self.blocks:
            if item.miner == address:
                balance += item.reward
        return balance

    def mine(self, miner):
        new_block = block([], 1 + self.last_number, self.last_hash)
        new_block.miner = miner
        new_block.reward = 100
        new_block.build()
        self.add(new_block)
    
    def save(self):
        blockchain_file = open(self.file_name, 'w')
        blockchain_file.write(str(self))
        blockchain_file.close()