#!/usr/bin/env python3

class block:
    def __init__(self, index, timestamp, transactions, previousHash):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous = previousHash