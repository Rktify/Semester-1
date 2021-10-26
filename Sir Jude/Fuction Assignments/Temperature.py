def convtemp():
    F = eval(input("Enter the temperature in Fahrenheit: "))
    C = 5/9*(F-32)
    print(f"The temperature in Fahrenheit is : {F}")
    print(f"The temperature in Celcius is : {C}")
    convK(C)

def convK(C):
    K = C + 273.15
    print(f"The temperature in Kelvin is : {K}")

convtemp()