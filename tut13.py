# Python Functions

# Python Keywords Reference: https://www.w3schools.com/python/python_ref_keywords.asp

def greeting():
    print("Hello World")

def palindrome():
    num = int(input("Enter a number:"))
    temp = num

    rev_num = 0

    while num != 0:
        rem = num%10
        rev_num = rev_num*10 + rem
        num //= 10

    if (temp == rev_num):
        print(f"{temp} is a palindrome number!")
    else:
        print(f"{temp} is not a palindrome number!")

def armstrong():
    num = int(input("Enter a number:"))
    temp = num

    sum2 = 0

    while num != 0:
        rem = num%10
        sum2 += rem**3
        num //= 10

    if (temp == sum2):
        print(f"{temp} is an armstrong number!")
    else:
        print(f"{temp} is not an armstrong number!")

def perfectNum():
    num = int(input("Enter a number:"))
    sum1 = 0

    for i in range(1, num+1):
        if i == num:
            break
        if num%i == 0:
            sum1 += i

    if (num == sum1):
        print(f"{num} is a perfect number!")
    else:
        print(f"{num} is not a perfect number!")

greeting()
# palindrome()
# armstrong()
perfectNum()