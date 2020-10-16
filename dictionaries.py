# print value
friend_ages = {
  "adam": 24,
  "liza": 28,
  "jonathan": 34
}

print(friend_ages["liza"])


# insert new key and value, and replace value
best_friend_ages = {
  "adam": 24,
  "liza": 28,
  "jonathan": 34
}

best_friend_ages["maya"] = 18
best_friend_ages["jonathan"] = 31
print(best_friend_ages)


# dictionary in tuples
friends = (
  {"name": "antonio", "age": 20},
  {"name": "lidya", "age": 28},
  {"name": "lorenzo", "age": 34}
)

print(friends[1]["name"])


# convert list of tuples to dictionary
friends = [("rio", 23), ("hanna", 28), ("elizabeth", 34)]
print(dict(friends))
