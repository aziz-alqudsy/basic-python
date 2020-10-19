doubled_numbers = [number * 2 for number in range(5)]
print(doubled_numbers)


numbers = [5 for _ in range(5)]
print(numbers)


friend_ages = [23, 34, 43, 45, 59]
age_strings = ["my friend age is {} years old".format(age) for age in friend_ages]

print(age_strings)


names = ["JonaThaN", "rOb", "AnGeLa"]
lower_names = [name.lower() for name in names]
upper_names = [name.upper() for name in names]

print(lower_names)
print(upper_names)


'''
checking string upper and lower case.
in this case, user input adam or ADAM,
but in the list is using Adam.
then setup output using title() func
that Upper case in first character
'''
friend = input("who is your friend? ")
friends = ["Adam", "Tatiana", "Albert"]
temp_friends = [name.lower() for name in friends]

if friend.lower() in temp_friends:
  print("your friend is {}".format(friend.title()))


#### with conditional ###

ages = [20, 21, 24, 27, 28]
odds = [age for age in ages if age % 2 == 1]

print(odds)


students = ["Rolf", "ruth", "charlie", "Jen"]
families = ["jose", "Bob", "rolf", "charlie", "Michael"]

# set
students_lower_set = set([student.lower() for student in students])
family_lower_set = set([family.lower() for family in families])

print(students_lower_set.intersection(family_lower_set))

# list
students_lower_list = [student.lower() for student in students]

present_friends = [
  name.title() for name in students_lower_list if name.lower() in families
]

print(present_friends)
