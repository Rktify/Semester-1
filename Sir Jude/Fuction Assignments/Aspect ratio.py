import math
def calcnh(w,h,dw):
    gcd = math.gcd(w,h)
    nw = w//gcd
    nh = h//gcd
    dh = nh/nw*dw
    return dh

width = eval(input("Enter the current width: "))
height = eval(input("Enter the current height: "))
dwidth = eval(input("Enter the desired width: "))
a = calcnh(width,height,dwidth)
print(f"The corresponding height is : {a}")