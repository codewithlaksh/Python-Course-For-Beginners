'''
Exercise 2: Generate n terms of a fibonacci series. Store them in a list. Display the list as well as the sum upto n terms of the series
'''

'''
0, 1, 1, 2, 3, 5, 8 ..... n terms

n (int) --> take input from the user
'''

lst = []
s = 0

a, b = 0, 1
lst.extend([a, b])

s = a + b

n = int(input("Enter the number of terms: "))

for i in range(0, n-2):
    c = a+b
    lst.append(c)
    s += c
    b = c
    a = b

print(f"The {n} terms of the fibonacci series are: {lst}")
print(f"The sum of {n} terms of the fibonacci series is: {s}")