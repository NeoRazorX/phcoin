#!/usr/bin/env python3

from .block import block

class blockchain:
    diff = 20
    max_nonce = 2**32
    target = 2 ** (256-diff)
    block = block("Genesis")
    dummy = head = block

    def add(self, block):
        block.previous_hash = self.block.hash()
        block.index = self.block.index + 1

        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        for n in range(self.max_nonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1