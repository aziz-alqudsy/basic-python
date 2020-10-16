x = True and False
print(x)


y = 35 and 0
print(y)
z = bool(35) and bool(0)
print(z)


a = True or False
print(a)


b = 35 or 0
print(b)
c = bool(35) or bool(0)
print(c)


name = ""
surename = "Smith"
greeting = name or surename
print(greeting)


'''
conclusion :
"and" gives you the first value if it is False,
otherwise it gives you the second value.

"or" gives you the first value if it is True,
otherwise it gives you the second value.
'''


number = int(input("choose your number? "))
validate = number > 0 and number < 10

print("your number is lower than 10? {}".format(validate))
