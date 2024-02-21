#This is meant to calculate volumes and surface areas of a cylinder and a sphere
#Date : 20/02/2024
#Name : Wachira Stanslaus

# cylinder
pi = 3.142
r = float(input("Enter the radius"))
h = float(input("Enter the height"))
r_sq = (r ** 2)

v = (pi * r_sq * h)
sa = ((2*pi*r*h) + (2*pi*r_sq))

print("The volume of the cylinder is ", v)
print("The surface area of the cylinder is ", sa)

# sphere
pi = 3.142
r = float(input("Enter the radius"))
r_sq = (r ** 2)
r_cd = (r ** 3)
a = (4 / 3)

v = a * pi * r_cd
sa = (4 * pi * r_sq)

print("The volume of the sphere is", v)
print("The surface area of the sphere is", sa)