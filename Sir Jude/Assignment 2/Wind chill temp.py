import math

temp = eval(input("Enter the temperature in Fahrenheit: "))

while temp > 41 or temp < -58:
    print("Temperature must be between -58F and 41F")
    temp = eval(input("Please re-enter the temperature in Fahrenheit: "))

v = eval(input("Enter the wind speed (mph): "))
while v <2:
    print("Speed must be greater than or equal to 2")
    v = eval(input("Please re-enter the wind speed (mph): "))

wci = ((35.74 + 0.6215*temp) - (35.75*(v**0.16)) + (0.4275*temp*(v**0.16)))

print("The wind chill index is %2.3f"%(wci))
