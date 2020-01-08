from functools import reduce
import hashlib as hl
from collections import OrderedDict
import json
import pickle

from hash_util import hash_string_256, hash_block
from block import Block

# Reward for the mining new block
MINING_REWARD = 10
blockchain = []
owner = 'Suraj'
participants = {'Suraj'}


def load_data():
    global blockchain
    global open_transactions
    try:
        with open('blockchain.txt', mode='r') as f:
            # file_content = pickle.loads(f.read())
            file_content = f.readlines()
            # blockchain = file_content['chain']
            # open_transactions = file_content['ot']
            blockchain = json.loads(file_content[0][:-1])
            update_blockchain = []
            for block in blockchain:
                converted_tx = [OrderedDict([
                        ('sender', tx['sender']), ('recipient', tx['recipient']), ('amount', tx['amount'])]) for tx in block['transactions']]
                update_block = Block(block.index, block.previous_hash, converted_tx, block.proof, block.timestamp)
                update_blockchain.append(update_block)
            blockchain = update_blockchain
            open_transactions = json.loads(file_content[1])
            updated_transactions = []
            for tx in open_transactions:
                updated_transaction = OrderedDict([('sender', tx['sender']),
                                                        ('recipient', tx['recipient']),
                                                        ('amount', tx['amount'])])
                updated_transactions.append(updated_transaction)
            open_transactions = updated_transactions
    except (IOError, IndexError):
        # Initializing out blockchain list
        genesis_block = Block(0, '', [], 100, 0)
        blockchain = [genesis_block]
        open_transactions = []
    finally:
        print('Clean up!')


load_data()


def save_data():
    try:
        with open('blockchain.txt', mode='w') as f:
            saveable_chain = [block.__dict__ for block in blockchain]
            f.write(json.dumps(saveable_chain))
            f.write('\n')
            f.write(json.dumps(open_transactions))
            # save_data = {
            #     'chain': blockchain,
            #     'ot': open_transactions
            # }
            # f.write(pickle.dumps(save_data))
    except IOError:
        print('Saving failed!')



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
    # Balance amount of the sender in block chain transactions
    tx_sender = [[tx['amount'] for tx in block.transactions if tx['sender'] == participant] for block in blockchain]
    # sum of amount by a sender in open transactions
    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)
    print(tx_sender)
    amount_sent = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)
    # amount received by the participant in block chain transactions
    tx_received = [[tx['amount'] for tx in block.transactions
                    if tx['recipient'] == participant] for block in blockchain]
    amount_received = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_received, 0)
    return amount_received - amount_sent


def get_last_blockchain_value():
    """ Returns last value of blockchain list"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']


def add_transaction(recipient, sender=owner, amount=1.0):
    """
    appends last value of block chain with new transaction

    :arguments:
    :sender: the sender of the coins
    :recipient: the recipient of the coins
    :amount: the amount of coins sent with the transaction ( default = 1.0 )

    """
    # transaction = {'sender': sender,
    #                'recipient': recipient,
    #                'amount': amount}
    transaction = OrderedDict([('sender', sender), ('recipient', recipient), ('amount', amount)])
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        save_data()
        return True
    return False


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    proof = proof_of_work()
    # reward_transaction = {
    #     'sender': 'MINING',
    #     'recipient': owner,
    #     'amount': MINING_REWARD
    # }
    reward_transaction = OrderedDict([('sender', 'MINING'), ('recipient', owner), ('amount', MINING_REWARD)])
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = Block(len(blockchain), hashed_block, copied_transactions, proof)
    blockchain.append(block)
    return True


def get_transaction_value():
    """ Returns user input as a float value
    """
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('your transaction amount please: '))
    return tx_recipient, tx_amount


def validate_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])


def get_user_choice():
    """ Returns user choice"""
    user_input=input('Your choice: ')
    return user_input


def print_blockchain_elements():
    """Print the block chain elements"""
    for block in blockchain:
        print('outputting block')
        print(block)
    else:
        print('-' * 20)


def verify_blockchain():
    """ verify the block chain and return True if valid """
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        elif block.previous_hash != hash_block(blockchain[index - 1]):
            return False
        if not valid_proof(block.transactions[:-1], block.previous_hash, block.proof):
            print('Proof of work is invalid!')
            return False
    return True


waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Display the blockchain blocks')
    print('4: Print the participants')
    print('5: check transaction validity')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        # Add the transaction amount to block chain
        if add_transaction(recipient, amount=amount):
            print('Added transaction!')
        else:
            print('Transaction failed!')
        print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
            save_data()
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)
    elif user_choice == '5':
        if validate_transactions():
            print('All transactions are valid')
        else:
            print('There are invalid transactions!')
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid. Please pick a value from the list')
    if not verify_blockchain():
        print_blockchain_elements()
        print('Invalid Blockchain!')
        break
    print('Balance of {} : {:6.2f}'.format(owner,get_balance(owner)))
else:
    print('User left!')


print('Done!')