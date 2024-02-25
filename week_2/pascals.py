# This is a program to show the pascal's triangle
# Date : 22/02/2024
# Name : Stanslaus

from math import factorial
n = int(input("Enter the number of rows :"))
for i in range(n):
    for j in range(i+1):
        print(end=" ")
        for j in range(i+1):
            print((factorial(i)//factorial(j)*factorial(i-j)), end = " ")
            print()
 
