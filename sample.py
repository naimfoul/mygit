import math

radius_str = input("Enter the radius of your choice")
radius_int = int(radius_str)

circumference = 2 * math.pi*radius_int
area = math.pi*(radius**2)

print("the circumference is:" ,circumference,\",and the area is",area)
