
friends = ["Hary", "Dik", "Joe", "Ann", "Marie"]

print(friends)

print(friends[0])
print(friends[-1])
print(friends[1:])
print(friends[1:3])

friends[1] = "Maanu"
print(friends)

friends.append("Jannet")
print(friends)

friends.insert(1,"Kelly")
print(friends)

friends.remove("Kelly")
print(friends)

lucky_num = [11, 22, 33, 12, 13]

friends.extend(lucky_num)
print(friends)
print(friends.index("Hary"))

friends.pop()
print(friends)

friends = ["Hary", "Dik", "Joe", "Ann", "Marie"]
friends.sort()
print(friends)

friends2 = friends.copy()
print(friends2)

friends.clear()
print(friends)
