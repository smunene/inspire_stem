
#write a function to print all prime no btn 1 and 99
#to print all squares and cubes btn 1 to 10
#calculate s.a of cylinder cone cube sphere and also0 their volumes

def print_square(first_no,last_no):
     for i in range(first_no,last_no+1):
        print(i**2)      
print_square(0,10)
print('\t')

def print_cube(first_no,last_no):
     for i in range(first_no,last_no+1):
        print(i**3)      
print_cube(0,10)


def is_prime(num):
    if num <=1:
        return False
       
s = float(input("Enter the side :" ))
def s_a_cube(s,):
    return ((s ** 6))
print(s_a_cube(s))

import math
pi = float(math.pi)

r = float(input("Enter the radius : "))
h = float(input("Enter the height : "))
def s_a_cylinder(r,h):
    return 2 * pi * r**2 + pi* 2*r *h
print(s_a_cylinder(r,h))

r = float(input("Enter the radius : "))
l = float(input("Enter the length : "))
def s_a_cone(r,l):
    return pi *r *l
print(s_a_cone(r,l))

r = float(input("Enter the radius : "))
def s_a_sphere(r):
    return 2 * pi * r**2
print(s_a_sphere(r))

r = float(input("Enter the radius : "))
def volume_sphere(r):
    return 4/3 * pi * r**3
print(volume_sphere(r))

r = float(input("Enter the radius : "))
h = float(input("Enter the height : "))
def volume_cone(r,h):
    return 1/3 * pi * r**2 *h
print(volume_cone(r,h))

r = float(input("Enter the radius : "))
h = float(input("Enter the height : "))
def volume_cylinder(r,h):
    return pi * r **2 * h
print(volume_cylinder(r,h))

s = float(input("Enter the side :" ))
def volume_cube(s):
    return s**3
print(volume_cube(s))

numbers = []
squares = []
cubes = []


start = 1
end = 10


for count in range(start, end + 1):
    numbers.append(count)
    squares.append(count** 2)
    cubes.append(count**3)


print("numbers: ", numbers)
print("squares: ", squares)
print("cubes  : ", cubes)
lower_value = int(input ("Please, Enter the Lowest Range Value: "))
upper_value = int(input ("Please, Enter the Upper Range Value: "))

print ("The Prime Numbers in the range are: ")
for number in range (lower_value, upper_value + 1):
    if number > 1:
        for i in range (2, number):
            if (number % i) == 0:
                break
        else:
            print (number)
