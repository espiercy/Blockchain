from functools import reduce
from collections import OrderedDict
import hashlib as hl

from hash_util import hash_string_256, hash_block

#init globals
MINING_REWARD = 10

genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': [],
    'proof': 100
}
blockchain = [genesis_block]
open_transactions = []

owner = 'Evan'
transaction_count = 0
participants = {'Evan'}

#functions
def valid_proof(transactions, last_hash, proof):
    guess = (str(transactions) + str(last_hash) + str(proof)).encode()
    guess_hash = hash_string_256(guess)
    print(guess_hash)
    return guess_hash[0:2] == '00'


def proof_of_work():
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0
    while not valid_proof(open_transactions, last_hash, proof):
        proof += 1
    return proof


def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)
    amount_sent = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)
    
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]
    amount_received = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_recipient, 0)
    return amount_received - amount_sent 


def get_last_blockchain_value():
    """ Returns the last value of current blockchain"""
    if len(blockchain) < 1:
       return None
    return blockchain[-1]


def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']


def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append latest value to previous block and push to open_blockchain
    
    Arguments:
       sender: sender of coins
       recipient: coin recipient
       amount: count of coins 
    
    """
    transaction = OrderedDict([('sender', sender), ('recipient', recipient), ('amount', amount)])
    if verify_transaction(transaction):      
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def mine_block():
    '''create a new block and add open transactions to it'''
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    proof = proof_of_work()
    #miners are to be rewarded
    reward_transaction = OrderedDict([('sender', 'MINING'),('recipient', owner),('amount', MINING_REWARD)])
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': copied_transactions,
        'proof': proof
    }
    blockchain.append(block)
    return True


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
    return input('''1: Add new transaction value
2: Mine a new block
3: Print blockchain
4: Print participants
5: Check transaction validity
h: Manipulate the chain
q: Quit
Choice: ''')


def print_blockchain():
    """ Print blockchain """
    for block in blockchain:
        print("Outputting Block: ")
        print(block)
    else:
        print('-' * 20)

def verify_chain():
    '''Verify if chain is still valid'''
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
        if not valid_proof(block['transactions'][:-1], block['previous_hash'], block['proof']):
            print('Proof of work is invalid')
            return False
    return True


def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])


waiting_for_input = True

while waiting_for_input:
    choice = get_user_choice()
    if choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        if add_transaction(recipient, amount=amount):
            print('Added transaction!')
        else:
            print('Transaction failed!')
        print(open_transactions)
    elif choice == '2':
        if mine_block():
            open_transactions = []
    elif choice == '3':
        print_blockchain()
    elif choice == '4':
        print(participants)
    elif choice == 'h':
        if len(blockchain)  >= 1:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'transactions': [{'sender': 'Chris', 'recipient': 'Evan', 'amount': 100.0}]
            }
    elif choice == '5':
        if verify_transactions():
            print('All transactions are valid.')
        else:
            print('There are invalid transactions.')
    elif choice == 'q':
        waiting_for_input = False
    else:
        print('Invalid choice! Choose again.')
    if not verify_chain():
        print_blockchain()
        print('Invalid blockchain!')
        break
    print('Balance of {}: {:6.2f}'.format('Evan', get_balance('Evan')))
    print()
else:
    print('User done!')


print('Goodbye!')