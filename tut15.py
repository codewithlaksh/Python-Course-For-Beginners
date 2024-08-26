# Function with non-default params
'''
def myfunc(a, b, ):
    print(a + b + c)
'''

# Function with default params
'''
def myfunc(a, b, c=10):
    print(a + b + c)
'''

'''
def myfunc(a, b, c): # Legal
def myfunc(a=10, b, c=10): # Illegal
def myfunc(a=10, b=10, c=10): # Legal
def myfunc(a, b=10, c=10): # Legal
'''

'''
def myfunc(a, b, c=15):
    print(a + b + c)
'''

# Positional arguments
# myfunc(2, 3, 12)

# Keyword arguments
# myfunc(b=10, c=20, a=20)

'''
def myfunc(*args):
    s = 0

    for i in args:
        s += i
    
    print("Sum:", s)

myfunc(10, 40, 30, 30, 10)
'''

def myfunc(**kwargs):
    s = 0
    # for key, value in kwargs.items():
    #     print(f'Key: {key} & Value: {value}')

    for i in kwargs.values():
        s += i

    print('Sum:', s)

myfunc(a=10, b=40, c=30, d=30, e=10)
