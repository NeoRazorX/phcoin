#!/usr/bin/env python3

from .block import block

class blockchain:
    last_hash = None
    last_number = 0

    def mine(self, miner):
        self.last_number += 1
        new_block = block([], self.last_number, self.last_hash)
        new_block.miner = miner
        new_block.reward = 100
        new_block.build()
        print(new_block)