# String In Python

'''
string = "Hello World \"Lakshyaraj\" "
string1 = 'Hello World \'Rohan\''
string2 = \'''Hello World '' "" \'''

print(string)
print(string1)
print(string2)
'''

string = "Lakshyaraj"

# print(string[0])
# print(string[20])
# print(string[len(string) - 1])
# print(string[-1])

# for i in string:
#     print(i)

# length = len(string)

'''
for i in range(length):
    print(string[i])
'''

'''
i = 0
while i < length:
    print(string[i])
    i += 1
'''

'''
print(string.upper())
print(string.lower())
print(string.isalnum())
print(string.isalpha())
print(string.isnumeric())

myName = "lakshyaraj"

my_name = "lakshyaraj"

MyName = "lakshyaraj"
'''

# var1 = "   this is a variable    "
# a = var1.rstrip()
# b = var1.lstrip()
# c = var1.strip()
# print(a)
# print(b)
# print(c)

# var2 = "this is a string"
# print(var2.split())
# var2 = "this,is,a,string"
# print(var2.split(',', 2))
# var2 = "this,is,a,string"
# print(var2.split(','))

# var2 = "this,is,a,string"
# print(var2.partition('t'))


# title = "This is my python tutorial"
# print(title.title())
# title = "this is my Python tutorial"
# print(title.capitalize())


# print(string[0:6])
# print(string[0:6:2])
# print(string[0:6:3])
# print(string[0:])
# print(string[0:20])

# print(string[-5:-1])
# print(string[-10:-1])
# print(string[::-1])
# print(string[-1:-11:-1])

# title = "this is my Python tutorial"
# print(title[0].upper() + title[1:])

# title = "this is my python tutorial"
# lst = title.split()
# new_title = ""

# for i in lst:
#     new_title += i[0].upper() + i[1:] + " "

# print(new_title)

# str1 = ",".join(['this', 'is', 'join', 'function'])
# print(str1)

name = "Lakshyaraj"
age = 18
# str2 = "My name is " + name
# str2 = "My name is {} and my age is {}".format(name, age)
str2 = f"My name is {name} and my age is {age}"

print(str2)
