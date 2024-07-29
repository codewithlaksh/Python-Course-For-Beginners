fruits = ["Apple", "Orange", "Guava", "Kiwi", "Grapes"]
# print(fruits)

# Mutable DataTypes: We can change the elements in place (list, dict)
'''
fruits[0] = "Cherry"
print(fruits)
'''
# Immutable DataTypes: We cannot change the elements in place (str, tuple)
'''
fruits_tup = ("Apple", "Orange", "Guava", "Kiwi", "Grapes")
fruits_tup[0] = "Cherry"
print(fruits_tup)
'''

# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print(fruits[3])
# print(fruits[4])

'''
for i in fruits:
    print(i)
'''

# for i in range(len(fruits)):
#     print(f'{i} - {fruits[i]}')

# fruits_sort = fruits.sort()
# fruits.sort()
# fruits.reverse()

# fruits.append("Peach")
# fruits.append(["Peach", "Watermelon"])
# fruits.extend("Peach")
# fruits.extend(["Peach", "Watermelon"])
# fruits.insert(-1, "Peach")
# fruits.insert(0, "Peach")

# fruits_sort = sorted(fruits)
# fruits_sort = sorted(fruits, reverse=True)
# print(fruits_sort)

# deleted = fruits.pop() # Removes last element
# deleted = fruits.pop(0)
'''
deleted = fruits.remove("Apple")
print(deleted) # Displays None in the console
'''
'''
fruits.remove("Apple")
print(fruits)
'''

# ind = fruits.index("")
'''
ind = fruits.index("Grapes")
print(ind)
'''
'''
count = fruits.count("Apple")
print(count)
'''

# print(fruits[2:])
# print(fruits[0:2])
# print(fruits[-5:-1:1])
# print(fruits[::-1])
