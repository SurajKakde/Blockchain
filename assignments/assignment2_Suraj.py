# 1) Create a list of names and use a for loop to output the length of each name (len()).
name_list = ['john','Maylie','Dash','Navin']
for name in name_list:
    print(name + ' ' + str(len(name)))
# 2) Add an if check inside the loop to only output names longer than 5 characters.
    if len(name) > 5:
        print('Names length greater than 5')
        print(name + ' ' + str(len(name)))
# 3) Add another if check to see whether a name includes a “n” or “N” character.
    if 'n' in name or 'N' in name:
        print('Name contains n or N: ' +name)
# 4) Use a while loop to empty the list of names (via pop())

while len(name_list) > 0:
    name_list.pop()
    print(name_list)

