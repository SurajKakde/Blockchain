# Initializing out blockchain list
blockchain = []

def get_last_blockchain_value():
    """ Returns last value of blockchain list"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction=[1]):
    """
    appends last value of block chain with new transaction

    :arguments:
    :transaction_amount: current transaction value
    :last_transaction: last transaction of the blockchain list (default [1])

    """
    if last_transaction is None:
        last_transaction = [1]
    blockchain.append([last_transaction,transaction_amount])


def get_transaction_value():
    """ Returns user input as a float value
    """
    return float(input('your transaction amount please: '))


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
    print('2: Display the blockchain blocks')
    print('h: Manipulate the transaction')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount=get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >=1 :
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid. Please pick a value from the list')
    if not verify_blockchain():
        print_blockchain_elements()
        print('Invalid Blockchain!')
        break
else:
    print('User left!')


print('Done!')