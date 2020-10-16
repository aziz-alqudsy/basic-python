frontend_member = {"liza", "robert", "mark"}
backend_member = {"lucas", "mark", "philip"}

frontend_member_not_fullstack = frontend_member.difference(backend_member)
backend_member_not_fullstack = backend_member.difference(frontend_member)
not_fullstack = frontend_member.symmetric_difference(backend_member)
fullstack = frontend_member.intersection(backend_member)
all_member = frontend_member.union(backend_member)

print("frontend member but not fullstack {}".format(frontend_member_not_fullstack))
print("backend member but not fullstack {}".format(backend_member_not_fullstack))
print("not fullstack member {}".format(not_fullstack))
print("fullstack {}".format(fullstack))
print("all member {}".format(all_member))
