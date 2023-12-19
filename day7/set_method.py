my_set = {1, 2, 3, 4, 5}
print(my_set)
my_set1 = {6,7,4, 5,8,10}

my_set.add(9)
print(my_set,"after add")

print(my_set.union(my_set1),"union")
print(my_set,"after union")


print(my_set.intersection(my_set1),"intersection")

print(my_set.difference(my_set1),"difference")

print(my_set)