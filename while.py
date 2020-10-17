# using break to stop looping
is_learning = True

while is_learning:
  print("I'm still learning")
  break


# using other statement to stop looping
hungry = True

while hungry:
  print("let's go eat")
  hungry = False


'''
value that not 'false'
or you input other value except 'false' is equal to true
in this case, you input 'yes' or 'no' to get always loop

thirsty = True

while thirsty:
  print(input("are you thirsty? "))

to fix it, you should initiate 'yes' equal to true
'''
thirsty = True

while thirsty:
  is_thirsty = input("are you thirsty? ")
  thirsty = is_thirsty == "yes"


# other case that convert boolean to string
user_input = input("Do you wish to run program? (y/n) ")

while user_input == "y":
  print("we are running!")
  user_input = input("Do you wish to run program again? (y/n) ")

print("we stopped running")
