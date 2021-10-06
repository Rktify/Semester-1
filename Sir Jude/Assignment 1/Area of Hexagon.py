import math
length = eval(input("Enter the side length of the hexagon: "))

area = (3*math.sqrt(3)/2)*(math.pow(length,2))

print(f"The area of a hexagon with the side length of {length} is %2.3f"%(area))