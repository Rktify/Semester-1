def convtday(): #This is the main function to input and for running the helper func
    global h, m, s #I used global to so the h, m, s variables can be calculated in another func
    h = float(input("Enter the amount of hours? : "))
    m = float(input("Enter the amount of minutes? : "))
    s = float(input("Enter the amount of seconds? : "))
    gdays()


def gdays(): #This is the helper function to do the calculations and the output
    days = (s/3600 + m/60 + h)/24
    print()
    print("The number of days is %2.4f"%(days)) #This is the output with the format

convtday()