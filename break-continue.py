running = ["ok", "ok", "fault", "ok"]

for status in running:
  if status == "fault":
    print("there is something fault")
    break
  print("running status is {0}".format(status))


infos = ("success", "fail", "success", "success")

for info in infos:
  if info == "fail":
    print("there is fail, skipping..")
    continue
  print("info is {}".format(info))
