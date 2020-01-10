from uuid import uuid4
from blockchain import Blockchain
from verification import Verification


class Node:
    def __init__(self):
        self.id = str(uuid4())
        self.blockchain = Blockchain(self.id)

    def get_transaction_value(self):
        """ Returns user input as a float value
        """
        tx_recipient = input('Enter the recipient of the transaction: ')
        tx_amount = float(input('your transaction amount please: '))
        return tx_recipient, tx_amount

    def get_user_choice(self):
        """ Returns user choice"""
        user_input = input('Your choice: ')
        return user_input

    def print_blockchain_elements(self):
        """Print the block chain elements"""
        for block in self.blockchain.chain:
            print('outputting block')
            print(block)
        else:
            print('-' * 20)

    def lister_for_input(self):
        waiting_for_input = True

        while waiting_for_input:
            print('Please choose')
            print('1: Add a new transaction value')
            print('2: Mine a new block')
            print('3: Display the blockchain blocks')
            print('4: check transaction validity')
            print('q: Quit')
            user_choice = self.get_user_choice()
            if user_choice == '1':
                tx_data = self.get_transaction_value()
                recipient, amount = tx_data
                # Add the transaction amount to block chain
                if self.blockchain.add_transaction(recipient, self.id, amount=amount):
                    print('Added transaction!')
                else:
                    print('Transaction failed!')
                print(self.blockchain.open_transactions)
            elif user_choice == '2':
                self.blockchain.mine_block(self.id)
            elif user_choice == '3':
                self.print_blockchain_elements()
            elif user_choice == '4':
                verifier = Verification()
                if verifier.validate_transactions(self.blockchain.open_transactions, self.blockchain.get_balance):
                    print('All transactions are valid')
                else:
                    print('There are invalid transactions!')
            elif user_choice == 'q':
                waiting_for_input = False
            else:
                print('Input was invalid. Please pick a value from the list')
            verifier = Verification()
            if not verifier.verify_blockchain(self.blockchain.chain):
                self.print_blockchain_elements()
                print('Invalid Blockchain!')
                break
            print('Balance of {} : {:6.2f}'.format(self.id , self.blockchain.get_balance()))
        else:
            print('User left!')

        print('Done!')


node = Node()
node.lister_for_input()