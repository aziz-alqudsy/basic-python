student_score = {
  "diana": 60,
  "robert": 80,
  "albert": 65
}

for name in student_score.keys():
  print(name)

for score in student_score.values():
  print(score)

for name, score in student_score.items():
  print("{0} got score {1}".format(name, score))
