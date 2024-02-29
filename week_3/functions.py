#A block of code running together as a unit
#eg sum(10,20)....10 and 20 are parameters of the function
#initialize(def) then call the function
#Types of functions : user defined and built in

#initializing the function
def print_name():
    print("My name is Wachira")
#calling the function
print_name()  

def print_details(name, age, id, gender):
    print("I am {0}, {1} years old. My id no is {2} and gender is {3}".format (name, age, id, gender))
print_details("Stans", "18", "21600887", "male")
print_details("Luise", "20", "21300000", "male")

def sum_nums(x,y):
    return x+y
z = sum_nums(10,20)
print(z)

def prod_nums(x,y):
    return x*y
print(prod_nums(5,10))


def print_odds(first_no, last_no):
    for i in range(first_no, last_no):
        print (i % 2)
print_odds(0,15)        
    


