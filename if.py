my_friend = "rudolf"
friend = input("Enter your name: ")

if friend == my_friend:
  print("hi {}, whats up?".format(my_friend))
elif friend == "":
  print("you should enter the name and run again")
else:
  print("hi {}, nice to meet you".format(friend))


# if statement on multi objects
friends = ["ralph", "dominic", "jonathan"]
family = ["alysa", "diana"]

name = input("enter your name: ")

if name in friends:
  print("hello {}, you're my friend".format(name))
elif name in family:
  print("hi {}, where is mom?".format(name))
elif name == "":
  print("you should enter the name and run again")
else:
  print("sorry, i don't know you")
