cars = ["ok", "ok", "ok"]

for car in cars:
  if car == "fault":
    print("there is fault car, skipping..")
  print("car is {}".format(car))
else:
  print("all cars built successfully, no fault car")
