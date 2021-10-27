import math
def calcnh(w,h,dw):
    gcd = math.gcd(w,h) #This GCD is for the ratio of the width and height
    nw = w//gcd
    nh = h//gcd
    dh = nh/nw*dw #From the ratio you can do simple math and find the desired height
    return dh

# These are the inputs for the user
width = eval(input("Enter the current width: "))
height = eval(input("Enter the current height: "))
dwidth = eval(input("Enter the desired width: "))

#For returning the a variable back
a = calcnh(width,height,dwidth)

# This is the output
print(f"The corresponding height is : {a}")