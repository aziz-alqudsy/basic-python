# looping in list, tuple or set
friends = ("anna", "liliana", "jake")

for friend in friends:
  print(friend)


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for _ in numbers:
  print (_)


students = [
  {"name": "ralph", "age": 24},
  {"name": "tika", "age": 20},
  {"name": "adrian", "age": 27}
]

for student in students:
  name = student["name"]
  age = student["age"]

  print("{0} has age {1}".format(name, age))


# looping range
for _ in range(3):
  print("hello world!")


for _ in range(2, 4):
  print(_)


for _ in range(0, 20, 3):
  print(_)
