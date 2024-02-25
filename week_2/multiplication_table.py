# This is a program to show the multiplication table
# Date : 22/02/2024
# Name : Wachira Stanslaus

num = int(input("Multiplication table of "))
for n in range ( 1 , 11):
    print(num, 'x', n, '=', num * n)

#Full set
# Multiplication table of numbers 1 - 9

for col in range (1, 10):
    for row in range (1, 10):
       print(row * col, end= '\t')
    print()