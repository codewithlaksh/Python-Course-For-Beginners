# range(start, stop [,step]) --> returns an object containing sequence of integers
'''
start --> the starting value of range function (inclusive), default value is 0
stop --> the last value of the range function (exclusive)
step --> increments each value of object (if provided), default value is 1
'''

# print(list(range(7)))

# for i in range(1, 8, 2):
#     print(i)

# for i in range(1, 8):
#     print(i)

# for i in range(8):
#     print(i)


# Jump statements --> continue, break
'''
for i in range(ord('A'), ord('Z')+1):
    if (chr(i) == 'E'):
        break
    print(i, ' - ', chr(i))
'''

'''
for i in range(ord('A'), ord('Z')+1):
    if (chr(i) == 'E' or chr(i) == 'O'):
        continue
    print(i, ' - ', chr(i))
'''

'''
for i in range(10):
    print(i)
else:
    print('Thank You!')
'''

'''
for i in range(10):
    if (i == 5):
        break
    print(i)
else:
    print('Thank You!')
'''

i = ord('A') # 65

while i <= ord('Z'): # 90
    if (chr(i) == 'E' or chr(i) == 'O'):
        i += 1
        continue
    print(i, ' - ', chr(i))
    i += 1

a = 20
while a <= 20:
    if (a == 15):
        break
    print(a)
    a -= 1
