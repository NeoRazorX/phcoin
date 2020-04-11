#!/usr/bin/env python3

import sys
from phcoinlib.blockchain import blockchain
from phcoinlib.wallet import wallet

def help():
    print("""
help        shows this dialog
history     shows the last transactions
info        shows the current wallet information
init        creates an empty wallet
mine        generates a new block
transfer    transfer coins from this wallet to another
update      downloads the last blocks from the blockchain
""")

def history():
    print("shows the last transactions")

def info():
    my_wallet = wallet()
    if not my_wallet.public_key:
        print("no wallet found. Use init to create one.")
    else:
        print("wallet: " + my_wallet.public_key)

def init():
    my_wallet = wallet()
    my_wallet.generate()
    print("new wallet: " + my_wallet.public_key)

def mine():
    my_wallet = wallet()
    my_blockchain = blockchain()
    my_blockchain.mine(my_wallet.public_key)

def transfer():
    print("transfer x yyyy")

def update():
    print("downloads the last blocks from the blockchain")

if __name__ == '__main__':
    if len(sys.argv) <= 1 or sys.argv[1] == 'help':
        help()
    elif sys.argv[1] == 'history':
        history()
    elif sys.argv[1] == 'info':
        info()
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