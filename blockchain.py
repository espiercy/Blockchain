#init globals
genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []

owner = 'Evan'
transaction_count = 0

#functions
def get_last_blockchain_value():
    """ Returns the last value of current blockchain"""
    if len(blockchain) < 1:
       return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append latest value to previous block and push to open_blockchain
    
    Arguments:
       sender: sender of coins
       recipient: coin recipient
       amount: count of coins 
    
    """
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    open_transactions.append(transaction)


def mine_block():
    last_block = blockchain[-1]
    hashed_block = '-'.join([str(last_block[key]) for key in last_block])
    print(hashed_block)
    for key in last_block:
        value = last_block[key]
        hashed_block = hashed_block + str(value)
    block = {'previous_hash': 'XYZ',
        'index': len(blockchain),
        'transactions': open_transactions
    }
    
    blockchain.append(block)


def get_transaction_value():
    """ Get input from user and add to blockchain """
    global transaction_count
    transaction_count +=1
    tx_recipient = input('Enter recipient name: ')
    tx_amount = float(input('Your transaction amount for ' + str(transaction_count) + ': '))
    return tx_recipient, tx_amount


def get_user_choice():
    """ Get user's option to proceed """
    print('Please choose an option: ')
    return input('1: Add new transaction value\n2: Mine a new block\n3: Print blockchain\nh: Manipulate the chain\nq: Quit\nChoice: ')


def print_blockchain():
    """ Print blockchain """
    for block in blockchain:
        print("Outputting Block: ")
        print(block)
    else:
        print('-' * 20)

def verify_chain():
    #block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break   
    #for block in blockchain:
    #    if block_index == 0:
    #        block_index += 1
    #        continue
    #    if block[0] == blockchain[block_index - 1]:
    #        is_valid = True
    #    else:
    #        is_valid = False
    #        break
    #    block_index += 1
    return is_valid


waiting_for_input = True

while waiting_for_input:
    choice = get_user_choice()
    if choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif choice == '2':
        mine_block()
    elif choice == '3':
        print_blockchain()
    elif choice == 'h':
        blockchain[0] = [2]
    elif choice == 'q':
        waiting_for_input = False
    else:
        print('Invalid choice! Choose again.')
    #if not verify_chain():
    #    print_blockchain()
    #    print('Invalid blockchain')
    #    break
    print()
else:
    print('User done!')


print('Goodbye!')