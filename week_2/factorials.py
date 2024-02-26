# This is a program to get factorials
# Date : 26/02/2024
# Name : Stanslaus

max_value = int(input("Enter the maximum number :"))
factorial_numbs = 1
for x in range (1,max_value + 1):
    factorial_numbs = factorial_numbs * x
    print(factorial_numbs)

#printing even numbers between 0 and 20
for i in range (0,20,2):
    print(i)

#printing odd numbers between 0 and 20
for i in range (1,20,2):
    print(i)