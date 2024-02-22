# strings in python
# Date : 22/02/2024
# Name : Stanslaus

city = "nairobi"

# convert to uppercase
print(city)
print("\n") #prints a new line
print(city.upper())

name = "WACHIRA STANSLAUS"
print(name)
print(name.lower()) #this converts string to lower case

town = "   Naivasha   "
print(town)
print("\t") #prints new tab
print(town.strip())

# add two strings
f_name = "Wachira"
s_name = "Stanslaus"
full_name = f_name + s_name
print(full_name)

print(city[0]) #prints n
print(city[1]) #prints a
print(city[2]) #i
print(city[3]) #r
print(city[4]) #o
print(city[5]) #b
print(city[6]) #i
print(city[-1])
print(city[-2])

#replacing a character
fruit = "Orange"
print(fruit.replace("O" , "Y"))

subject = "Physical:Sciences"
print(subject.split(":"))

age = 18
height = 1.2
print("I am {0} years old and {1} metres tall" .format(age , height))



