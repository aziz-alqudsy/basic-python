# calling list
data = ["antonio", 2, "sebastian"]
print(data[1])

friends = [["diana", 24], ["jack", 28], ["liza", 30]]
print(friends[0][0])


# adding value at the last in list
number = [1, 2, 3]
number.append(4)
number.remove(2)
print(number)


# adding value in some index list
data = [1, 3, 4]
temp = data[:]
print(temp)
temp[1:1] = [2]
print(temp)


# calling key in json list
json ={
  "sudent": "aziz",
  "class": "kelas-i"
}

temp = []

for k,v in json.items():
  temp.append(k)

print(temp[1])
