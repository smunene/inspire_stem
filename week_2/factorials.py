# This is a program to show factorials
# Date : 22/02/2024
# Name : Wachira Stanslaus

import math

n = int(input("Enter the number whose factorial u want to find : "))

print ("The factorial is :", math.factorial (n)) # This is a built in function in python for finding factorial of number n

# Using for loop

factorial = int(input("Enter the number whose factorial u want to find : "))
n = 1

if factorial >=1:
    for i in range (1, n+2):

        factorial_ans = factorial * i

print ("The factorial is :", factorial_ans)      