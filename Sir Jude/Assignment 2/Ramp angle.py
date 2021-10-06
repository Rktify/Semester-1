import math

g = 9.8

mass = eval(input("Enter the mass of the cart (in kg): "))
force = eval(input("Enter the force to push the cart (in N): "))

angle = math.sinh(force/(mass*g))
degree = math.degrees(angle)

print("The angle of the ramp is %2.1f degrees"%(degree))