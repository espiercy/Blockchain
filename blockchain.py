#init globals
blockchain = []
transaction_count = 0

#functions
def get_last_blockchain_value():
    """ Returns the last value of current blockchain"""
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """ Append latest value to previous block and push to blockchain
    
    Arguments:
       transaction_amount: The amount to be added
       last_transaction: The previous blockchain transaction (default [1]) 
    
    """
    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    """ Get input from user and add to blockchain """
    global transaction_count
    transaction_count +=1
    tx_amount = float(input('Your transaction amount for ' + str(transaction_count) + ': '))
    add_value(tx_amount)
    print(blockchain)


tx_total_count = int(input("Enter the number of transactions you wish to complete: "))

for i in range(tx_total_count):
    get_user_input()
