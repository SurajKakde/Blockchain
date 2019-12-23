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
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    tx_received = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]
    amount_received = 0
    for tx in tx_received:
        if len(tx) > 0:
            amount_received += tx[0]
    return amount_received - amount_sent


def get_last_blockchain_value():
    """ Returns last value of blockchain list"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


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
    open_transactions.append(transaction)
    participants.add(sender)
    participants.add(recipient)


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    block = {'previous_hash': hashed_block,
             'index': len(blockchain),
             'transactions': open_transactions}
    blockchain.append(block)
    return True


def get_transaction_value():
    """ Returns user input as a float value
    """
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('your transaction amount please: '))
    return tx_recipient, tx_amount


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
    print('h: Manipulate the transaction')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data=get_transaction_value()
        recipient , amount = tx_data
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)
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
    print(get_balance('Suraj'))
else:
    print('User left!')


print('Done!')