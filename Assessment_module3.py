# 1) Create a list of “person” dictionaries with a name, age and list of hobbies for each person. Fill in any data you want.
person_info = [{'name': 'Bob', 'age': 18,'hobbies': ['skiing', 'reading', 'movies']},
               {'name': 'Maria', 'age': 22,'hobbies': ['reading', 'Dancing']},
               {'name': 'Mike', 'age': 24,'hobbies': ['singing', 'Dancing']},
               {'name': 'Chris', 'age': 21,'hobbies': ['kite boarding', 'reading', 'cycling']}
               ]
print(person_info)

# 2) Use a list comprehension to convert this list of persons into a list of names (of the persons).
person_names = [person['name'] for person in person_info]
print(person_names)

# 3) Use a list comprehension to check whether all persons are older than 20.
if all([person['age'] > 20 for person in person_info]):
    print('Yes! Age of all persons is greater than 20')
else:
    print('No! Age of all persons is not greater than 20')


# 4) Copy the person list such that you can safely edit the name of the first person (without changing the original list).
# copied_persons = persons[:]
#copied_persons = person_info[:]
copied_persons = [p.copy() for p in person_info]
copied_persons[0]['name'] = 'Suraj'
print(copied_persons)
print(person_info)


# 5) Unpack the persons of the original list into different variables and output these variables.
name1,name2,name3,name4 = person_names
print(name1 + '\n' + name2 + '\n' + name3 + '\n' + name4)
