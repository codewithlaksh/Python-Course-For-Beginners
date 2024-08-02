fruits_tup = ("Apple", "Orange", "Guava", "Kiwi", "Grapes")
t = (1,)

print(type(t))

'''
fruits_tup = list(fruits_tup)
fruits_tup[0] = "Cherry"

fruits_tup = tuple(fruits_tup)
print(fruits_tup)
'''

# a, b, c, d, e, f = fruits_tup # ValueError
# a, b, c, d, e = fruits_tup
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)

'''
for i in fruits_tup:
    print(i)
'''

# fruits_tup.sort() # AttributeError
# a = tuple(sorted(fruits_tup))
# print(a)
# fruits_tup.reverse() # AttributeError

# ind = fruits_tup.index('Cherry') # ValueError
# ind = fruits_tup.index('Apple')
# print(ind)

# print(fruits_tup[7]) # IndexError
# print(fruits_tup[-1])
# print(fruits_tup[0:2])
# print(fruits_tup[0:2:2])

# print(fruits_tup.count('a')) # 0
print(fruits_tup.count('Apple'))

# fruits_tup.insert()
