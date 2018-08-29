#init globals
blockchain = []
transaction_count = 0

#functions
def get_last_blockchain_value():
    """ Returns the last value of current blockchain"""
    if len(blockchain) < 1:
       return None
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """ Append latest value to previous block and push to blockchain
    
    Arguments:
       transaction_amount: The amount to be added
       last_transaction: The previous blockchain transaction (default [1]) 
    
    """
    if last_transaction == None:
        last_transaction = [1]
    else:
        blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    """ Get input from user and add to blockchain """
    global transaction_count
    transaction_count +=1
    tx_amount = float(input('Your transaction amount for ' + str(transaction_count) + ': '))
    if blockchain != []:
        add_value(tx_amount, get_last_blockchain_value())
    else:
        add_value(tx_amount)


def get_user_choice():
    print('Please choose an option: ')
    return input('1: Add new transaction value\n2: Print blockchain\nq: Quit\nChoice: ')


def print_blockchain():
    for block in blockchain:
        print("Outputting Block: ")
        print(block)


while(True):
    choice = get_user_choice()
    if choice == '1':
        get_user_input()
    elif choice == '2':
        print_blockchain()
    elif choice == 'q':
        break
    else:
        print('Invalid choice! Choose again.')
    print()


print('Goodbye!')