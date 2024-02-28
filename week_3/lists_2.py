friends = ["Kate" , "Lorna" , "Shee" , "Shix" , "Stans"]
for friend in friends :
    print(friend)

enemies = friends[:]    #to copy one list into another
print (enemies)

fruits = ["guava" , "mango" , "orange" , "apple" , "berries"]
#slice the list to get part of the list
print(fruits[0:3])

del fruits[0]
print(fruits)

squares = [] #initializes an empty list
for x in range(0,11) :
    squares.append(x**2)
print(squares)    