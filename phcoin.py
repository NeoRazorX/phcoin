import sys

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
    print("history")

def init():
    print("init")

def mine():
    print("mine")

def transfer():
    print("transfer x yyyy")

def update():
    print("update")

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