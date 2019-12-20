# Initializing out blockchain list
genesis_block = {'previous_hash': '',
             'index': 0,
             'transactions': []}
blockchain = [genesis_block]
open_transactions = []
owner = 'Suraj'

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



def mine_block():
    last_block = blockchain[-1]
    hashed_block = '-'.join(str(last_block[keys]) for keys in last_block)
    print(hashed_block)
    block = {'previous_hash': hashed_block,
             'index': len(blockchain),
             'transactions': open_transactions}
    blockchain.append(block)


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
    block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
    #         break
    # for block in blockchain:
    #     if block_index == 0:
    #         block_index += 1
    #         continue
    #     elif block[0] == blockchain[block_index - 1]:
    #         is_valid = True
    #     else:
    #         is_valid = False
    #         break
    #     block_index += 1
    return is_valid


waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('2: Display the blockchain blocks')
    print('h: Manipulate the transaction')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data=get_transaction_value()
        recipient , amount = tx_data
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        mine_block()
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >=1 :
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid. Please pick a value from the list')
    # if not verify_blockchain():
    #     print_blockchain_elements()
    #     print('Invalid Blockchain!')
    #     break
else:
    print('User left!')


print('Done!')