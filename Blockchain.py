import functools
#reward for the mining new block
MINING_REWARD = 10
# Initializing out blockchain list
genesis_block = {'previous_hash': '',
             'index': 0,
             'transactions': []}
blockchain = [genesis_block]
open_transactions = []
owner = 'Suraj'
participants = {'Suraj'}


def hash_block(block):
    return '-'.join([str(block[keys]) for keys in block])


def get_balance(participant):
    # Balance amount of the sender in block chain transactions
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
    # sum of amount by a sender in open transactions
    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)
    print(tx_sender)
    amount_sent = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)
    # amount received by the participant in block chain transactions
    tx_received = [[tx['amount'] for tx in block['transactions']
                    if tx['recipient'] == participant] for block in blockchain]
    amount_received = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_received, 0)
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
    transaction = {'sender': sender,
                   'recipient': recipient,
                   'amount': amount}
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': MINING_REWARD
    }
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = {'previous_hash': hashed_block,
             'index': len(blockchain),
             'transactions': copied_transactions}
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
        elif block['previous_hash'] != hash_block(blockchain[index - 1]):
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
    print('h: Manipulate the transaction')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data=get_transaction_value()
        recipient , amount = tx_data
        # Add the transaction amount to block chain
        if add_transaction(recipient, amount=amount):
            print('Added transaction!')
        else:
            print('Transaction failed!')
        print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)
    elif user_choice == '5':
        if validate_transactions():
            print('All transactions are valid')
        else:
            print('There are invalid transactions!')
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {'previous_hash': '',
             'index': 0,
             'transactions': [{'sender':'Suraj', 'recipient':'Dinga', 'amount':100}]}
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