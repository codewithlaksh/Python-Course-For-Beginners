'''
Flow of execution:
1. Reads the variables. In case of a function, it reads the header of the function.
2. Ignores the comments written in the code.
3. When the function is called, it jumps to the statement where the function is defined.
4. If there is any return statement in the function, it jumps back again to the step where the function has been called.
'''
# Local scoped variables
'''
# 11 -> 14 -> 11 -> 12 -> 13
def myname():
    name = input("Enter your name: ")
    print(name)
myname()

# 17 -> 20 -> 17 -> 18 -> 19 -> 20
def myname():
    name = input("Enter your name: ")
    return name
print(myname())
'''

# Global variables
'''
name = input("Enter your name: ")
def myname():
    # name = input("Enter your name: ")
    print(name)
print(f"My Name: {name}")
myname()
'''

# Access local scoped variables globally
def myname():
    global name
    name = input("Enter your name: ")
    print(name)
myname()
print(f"My Name: {name}")