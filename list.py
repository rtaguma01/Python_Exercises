#Practice List

list = ["apple", "banana", "pear", "orange", "strawberry"]
length = len(list)
print length
print ("\n")

list.append("grapes")
print list

list.insert(2,"cantaloupe")
print list

list.remove("orange")
print list


list2 = ["peas", "carrots", "lettuce", "beets"]
list.extend(list2)
print list

del list[2]
print list

print sorted(list)
print list


