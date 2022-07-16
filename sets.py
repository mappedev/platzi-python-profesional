set1 = {1, 2, 3}
set2 = {3, 4, 5}

# print("sets union:", set1 | set2)
print("sets union", set1.union(set2))

# print("sets interception:", set1 & set2)
print("sets interception:", set1.intersection(set2))

# print("set1 difference at set2:", set1 - set2)
print("set1 difference at set2:", set1.difference(set2))

# print("set2 difference at set1:", set2 - set1)
print("set2 difference at set1:", set2.difference(set1))

# print("sets symetric difference:", set1 ^ set2)
print("sets symetric difference:", set1.symmetric_difference(set2))
