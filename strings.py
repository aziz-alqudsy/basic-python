# direct string
print("direct string")


# string variable
my_string = "string variable"
print(my_string)


# string with quotes
single_quote = 'single quote'
print(single_quote)

double_quotes = "double quotes"
print(double_quotes)

multi_quotes = 'this is single quote and "this is double quotes"'
print(multi_quotes)

escaping_quotes = "this is \"escaping quotes\""
print(escaping_quotes)


# multiline string
multiline = '''first line

second line'''
print(multiline)


# convert integer to string
age = 28
int_to_str = str(age)
print("my age is " + int_to_str)


# string formatting
age = 28
print(f"my age is {age}")

name = "Aziz"
greeting = f"hello {name}!"
print(greeting)

morning = "morning"
greeting = "good {}!"
good_morning = greeting.format(morning)
print(good_morning)
evening = "evening"
good_evening = greeting.format(evening)
print(good_evening)

day = "day"
greeting = "good {time}!"
good_day = greeting.format(time=day)
print(good_day)
