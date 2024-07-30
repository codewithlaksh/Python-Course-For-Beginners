# Solution to exercise 1

# Take a number as input from and check if the number is perfect number, armstrong number or palindrome
'''
Perfect Number: a number which is equal to the sum of its prime factors.
Armstrong Number: a number which is equal to the sum of cubes of its digits
Palindrome Number: a number which is equal to the reverse of that number
'''

'''----- ANSWER -----'''

num = int(input("Enter a number:"))
temp = num

# Checking for perfect number
'''
sum1 = 0

for i in range(1, num+1):
    if i == num:
        break
    if num%i == 0:
        sum1 += i

if (num == sum1):
    print(f"{temp} is a perfect number!")
else:
    print(f"{temp} is not a perfect number!")
'''


# Checking for armstrong number
'''
sum2 = 0

while num != 0:
    rem = num%10
    sum2 += rem**3
    num //= 10

if (temp == sum2):
    print(f"{temp} is an armstrong number!")
else:
    print(f"{temp} is not an armstrong number!")
num = temp
'''

# Checking for palindrome number

rev_num = 0

while num != 0:
    rem = num%10
    rev_num = rev_num*10 + rem
    num //= 10

if (temp == rev_num):
    print(f"{temp} is a palindrome number!")
else:
    print(f"{temp} is not a palindrome number!")

