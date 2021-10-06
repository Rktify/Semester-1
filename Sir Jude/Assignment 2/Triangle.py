edge1 = eval(input("Enter the length of the 1st edge of the triangle : "))
edge2 = eval(input("Enter the length of the 2nd edge of the triangle : "))
edge3 = eval(input("Enter the length of the 3rd edge of the triangle : "))
if(edge1+edge2 >= edge3) and (edge1+edge3 >= edge2) and (edge2+edge3 >= edge1):
    perimeter = edge1+edge2+edge3
    print("The perimeter of your triangle is", perimeter)
else:
    print("The perimeter cannot be calculated. Your input is invalid, please retry")