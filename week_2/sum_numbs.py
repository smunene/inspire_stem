# This is a program to get the sum of the first 20 numbers
# Date : 26/02/2024
# Name : Stanslaus

max_value = int(input("Enter the maximum number :"))
sum_numbs = 0
for x in range (0,max_value + 1):
    sum_numbs = sum_numbs + x
    print(sum_numbs)