# This is a program showing employee records
# Date : 21/02/2024
# Name : Wachira Stanslaus

name = input("Enter employee name")
age = input("Enter employee age")
salary = int(input("Enter employee salary"))
bonus = float(input("Enter employee bonus"))
percentage = (30/100)

inc = salary + (salary * percentage)

print("The employee name is" ,name)
print("The employee age is" ,age)
print("The employee salary is" ,salary)
print("The employee bonus is" ,bonus)
print("The employee increased salary is" ,inc)

ded = 5000
new_bonus = bonus - ded

print("The employee new bonus is" ,new_bonus)