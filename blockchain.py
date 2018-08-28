blockchain = []
transaction_count = 0

def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])


def ask_input():
    global transaction_count
    transaction_count +=1
    tx_amount = float(input('Your transaction amount for ' + str(transaction_count) + ': '))
    add_value(tx_amount)
    print(blockchain)


tx_total_count = int(input("Enter the number of transactions you wish to complete: "))

for i in range(tx_total_count):
    ask_input()
