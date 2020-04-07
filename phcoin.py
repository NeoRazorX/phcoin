#!/usr/bin/env python3

import sys
from lib.wallet import wallet

def help():
    print("""
help        shows this dialog
history     shows the last transactions
init        creates an empty wallet
mine        generates a new block
transfer    transfer coins from this wallet to another
update      downloads the last blocks from the blockchain
""")

def history():
    print("shows the last transactions")

def init():
    print("creates an empty wallet")
    mywallet = wallet()
    mywallet.generate()
    print(mywallet.publicKey)

def mine():
    print("generates a new block")

def transfer():
    print("transfer x yyyy")

def update():
    print("downloads the last blocks from the blockchain")

if __name__ == '__main__':
    if len(sys.argv) <= 1 or sys.argv[1] == 'help':
        help()
    elif sys.argv[1] == 'history':
        history()
    elif sys.argv[1] == 'init':
        init()
    elif sys.argv[1] == 'mine':
        mine()
    elif sys.argv[1] == 'transfer':
        transfer()
    elif sys.argv[1] == 'update':
        update()
    else:
        help()