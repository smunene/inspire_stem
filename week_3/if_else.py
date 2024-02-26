#This is a program to show if comments
#Date:26/02/2024
#Name:Wachira

age = 25
if age > 18:
    print("You are allowed to drive")

sal = 45000
if sal > 30000 and sal < 50000:
    salary = sal * 0.1 + sal
    print(salary)

home_county = "Nyeri"
if home_county == "Nyeri" or home_county == "Kiambu":
    print("You get a bursary")

grade = 70
if grade > 84 :
    print("You win a calculator")
else  :
    print("You repeat the class")

grade = 70
if grade >= 84 and grade <=90 :
    print("You win a calculator")
elif grade >= 50 and grade <=83 :
    print("You win a mathematical set")
else :
    print("You get nothing !")