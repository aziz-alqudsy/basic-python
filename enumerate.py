friends = ["john", "anna", "elizabeth"]

for counter, friend in enumerate(friends):
  print(counter)
  print(friend)

'''
enumerate always start with 0
 but it can set with number you want
'''
for counter, friend in enumerate(friends, start=5):
  print(counter)
  print(friend)

# convert to list
print(list(enumerate(friends)))

# convert to dictionary
print(dict(enumerate(friends)))

# zip is same as enumerate
print(list(zip([0, 1, 2], friends)))
