from uuid import uuid4
from blockchain import Blockchain
from verification import Verification


CHOICE_STRING = '''1: Add new transaction value
2: Mine a new block
3: Print blockchain
4: Check transaction validity
q: Quit
Choice: '''

class Node:
    def __init__(self):
        #self.id = str(uuid4())
        self.id = 'EVAN'
        self.blockchain = Blockchain(self.id)


    def get_transaction_value(self):
        """ Get input from user and add to blockchain """
        tx_recipient = input('Enter recipient name: ')
        tx_amount = float(input('Your transaction amount: '))
        return tx_recipient, tx_amount


    def get_user_choice(self):
        """ Get user's option to proceed """
        print('Please choose an option: ')
        return input(CHOICE_STRING)


    def print_blockchain(self):
        """ Print blockchain """
        for block in self.blockchain.chain:
            print("Outputting Block: ")
            print(block)
        else:
            print('-' * 20)


    def listen_for_input(self):
        waiting_for_input = True
        while waiting_for_input:
            choice = self.get_user_choice()
            if choice == '1':
                tx_data = self.get_transaction_value()
                recipient, amount = tx_data
                if self.blockchain.add_transaction(recipient, self.id, amount=amount):
                    print('Added transaction!')
                else:
                    print('Transaction failed!')
                print(self.blockchain.get_open_transactions())
            elif choice == '2':
                self.blockchain.mine_block()
            elif choice == '3':
                self.print_blockchain()
            elif choice == '4':
                if Verification.verify_transactions(self.blockchain.get_open_transactions(), self.blockchain.get_balance):
                    print('All transactions are valid.')
                else:
                    print('There are invalid transactions.')
            elif choice == 'q':
                waiting_for_input = False
            else:
                print('Invalid choice! Choose again.')
            if not Verification.verify_chain(self.blockchain.chain):
                self.print_blockchain()
                print('Invalid blockchain!')
                break
            print('Balance of {}: {:6.2f}'.format(self.id, self.blockchain.get_balance()))
            print()
        else:
            print('User done!')


node = Node()
node.listen_for_input()
