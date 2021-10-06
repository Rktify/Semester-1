x1 = eval(input("Enter the x-coordinate for point 1: "))
x2 = eval(input("Enter the x-coordinate for point 2: "))
y1 = eval(input("Enter the y-coordinate for point 1: "))
y2 = eval(input("Enter the y-coordinate for point 2: "))

slope = (y2-y1)/(x2-x1)

print(f"The slope for the line that connects the 2 points ({x1}, {y1}) and ({x2}, {y2}) is %2.5f" % (slope))