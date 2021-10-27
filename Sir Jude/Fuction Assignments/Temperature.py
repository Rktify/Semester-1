def convtemp(): #This is the main function that takes no arguments
    F = eval(input("Enter the temperature in Fahrenheit: "))
    C = 5/9*(F-32)
    print(f"The temperature in Fahrenheit is : {F}")
    print(f"The temperature in Celcius is : {C}")
    convK(C) #You call the convert Kelvin function with 1 argument

def convK(C): #This function takes 1 argument to count Kelvin
    K = C + 273.15
    print(f"The temperature in Kelvin is : {K}")

convtemp()