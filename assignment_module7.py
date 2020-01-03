import json
import pickle

# 1) Write a short Python script which queries the user for input (infinite loop with exit possibility) and writes the input to a file.
# 3) Store user input in a list (instead of directly adding it to the file) and write that list to the file – both with pickle and json.


def write_file(input):
    # with open('assignment_data.txt', mode='a') as f:
    #     f.write(input + '\n')
    with open('assignment_m7.json', mode='w') as f1:
        f1.write(json.dumps(input))
    with open('assignment_m7.p', mode='wb') as f2:
        f2.write(pickle.dumps(input))


# 2) Add another option to your user interface: The user should be able to output the data stored in the file in the terminal.
def read_file():
    with open('assignment_m7.json', mode='r') as f:
        file_content = f.read()
        print(json.loads(file_content))
        # for line in file_content:
        #     print(line)

# 4) Adjust the logic to load the file content to work with pickled/ json data.
with open('assignment_m7.p', mode='rb') as f:
    file_content = f.read()
    stored_data = pickle.loads(file_content)
    input_list = stored_data

ui = True
while ui:
    print('Please choose')
    print('1: for user input')
    print('2: display file')
    print('q: Quit')
    ui = input('you option:')
    if ui == '1':
        user_input = input('Please enter input: ')
        input_list.append(user_input)
        write_file(input_list)
    elif ui == '2':
        read_file()
    elif ui == 'q':
        ui = False
print('Done!')





