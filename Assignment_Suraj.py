# collecting input from the user for name and age
name=input('Please enter your name: ')
age=input('Please enter your age: ')


def my_intro(name, age):
    """ Concatenate the name and age and print"""
    print('Hello! My name is '+name+' and my age is ' +age)


def add_strings(string1, string2):
    """concatenates two random strings
    """
    print(string1 + ' ' + string2)


def decades_lived(age):
    """returns the number of decades lived
    Arguments:
        :age: Age fo the person
    """
    return int(age) // 10


my_intro(name, age)

add_strings('hello', 'world')

print(name + ' already lived '+ str(decades_lived(age)) + ' decades.')
