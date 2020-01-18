from blockchain import Blockchain
from utility.verification import Verification
from wallet import Wallet


class Node:
    def __init__(self):
        # self.id = str(uuid4())
        self.wallet = Wallet()
        self.wallet.create_keys()
        self.blockchain = Blockchain(self.wallet.public_key)
        
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
            print('5: create wallet')
            print('6: load wallet')
            print('7: save wallet')
            print('q: Quit')
            user_choice = self.get_user_choice()
            if user_choice == '1':
                tx_data = self.get_transaction_value()
                recipient, amount = tx_data
                # Add the transaction amount to block chain
                signature = self.wallet.sign_transaction(self.wallet.public_key, recipient, amount)
                if self.blockchain.add_transaction(recipient, self.wallet.public_key, signature, amount=amount):
                    print('Added transaction!')
                else:
                    print('Transaction failed!')
                print(self.blockchain.get_open_transaction())
            elif user_choice == '2':
                if not self.blockchain.mine_block(self.wallet.public_key):
                    print('Mining failed. got no wallet?')
            elif user_choice == '3':
                self.print_blockchain_elements()
            elif user_choice == '4':
                if Verification.validate_transactions(self.blockchain.get_open_transaction(), self.blockchain.get_balance):
                    print('All transactions are valid')
                else:
                    print('There are invalid transactions!')
            elif user_choice == '5':
                self.wallet.create_keys()
                self.blockchain = Blockchain(self.wallet.public_key)
            elif user_choice == '6':
                self.wallet.load_keys()
                self.blockchain = Blockchain(self.wallet.public_key)
            elif user_choice == '7':
                self.wallet.save_keys()
            elif user_choice == 'q':
                waiting_for_input = False
            else:
                print('Input was invalid. Please pick a value from the list')
            if not Verification.verify_blockchain(self.blockchain.chain):
                self.print_blockchain_elements()
                print('Invalid Blockchain!')
                break
            print('Balance of {} : {:6.2f}'.format(self.wallet.public_key, self.blockchain.get_balance()))
        else:
            print('User left!')

        print('Done!')


if __name__ == '__main__':
    node = Node()
    node.lister_for_input()
