# sets
friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "rolf", "Charlie", "michael"]

friends_lower = {friend.lower() for friend in friends}
guests_lower = {guest.lower() for guest in guests}

intersection_friends = friends_lower.intersection(guests_lower)
present_friends = {name.title() for name in intersection_friends}

print(present_friends)


# dictionaries
students = ["Rolf", "Bob", "Jane", "Anne"]
ages = [23, 43, 12, 43]

biodata = {
  students[i]: ages[i]
  for i in range(len(students))
}

print(biodata)


unmarried_students = {
  students[i]: ages[i]
  for i in range(len(students))
  if ages[i] < 25
}

print(unmarried_students)
