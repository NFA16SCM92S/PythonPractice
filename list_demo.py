friends = ["Kara", "Violet", "Eric", "Eric", "James", "Aarav", "Aria", "Ananya"]
lucky_numbers = [22,345,30,14,4,622,70,98]
print(friends)
print(friends[1])
print(friends[-1])
print(friends[4:])
print(friends[1:4])
friends.sort()
print(friends)
friends.reverse()
print(friends)
#add two list together
friends.extend(lucky_numbers)
print(friends)
print(friends.count("Eric"))
friends2 = friends.copy()
print(friends2)
#append
friends.append("Charlie")
print(friends)
#insert
friends.insert(1, "Kelly")
print(friends)
#remove
friends.remove("James")
print(friends)
#check if element is in list or not
print(friends.index("James"))
friends.clear()
print(friends)

