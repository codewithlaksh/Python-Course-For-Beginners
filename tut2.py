# Variables & Datatypes

'''
DataTypes: str, int, float, tuple, list, dict, set, complex
'''

# 1var = "" # SyntaxError
var1 = "Lakshyaraj Dash" # str
var2 = 23 # int
var3 = 23.5 # float
var4 = (1, 2, 3) # tuple
var5 = [1, 2, 3, 4, 5] # list
var6 = {1: 'One', 2: 'Two'} # dict
var7 = {1, 2, 3} # set
var8 = 1 + 2j # complex
Var1 = "Rohan"
# print(var1)
# print(Var1)

# my$name = "Sahil" # SyntaxError
my_name = "Sahil"
# print(my_name)

# print(type(var1))
# print(type(var2))
# print(type(var3))
# print(type(var4))
# print(type(var5))
# print(type(var6))
# print(type(var7))
# print(type(var8))

'''
Rules to declare variables:
1. Variables are case sensitive.
2. Variables cannot start with number. Throws SyntaxError
3. Variables can contain numbers in between or at the end.
4. Only underscores (_) are allowed.
'''

a = 4
b = str(4)
# b = tuple(4) # TypeError
# print(b)
c = list('Chandrayaan-2')
# print(c)
d = dict.fromkeys('Chandrayaan-2')
# print(d)
e = tuple('Chandrayaan-2')
# print(e)
f = set('Chandrayaan-2')
print(f)
