def convtday():
    global h, m, s
    h = float(input("Enter the amount of hours? : "))
    m = float(input("Enter the amount of minutes? : "))
    s = float(input("Enter the amount of seconds? : "))
    gdays()


def gdays():
    days = (s/3600 + m/60 + h)/24
    print()
    print("The number of days is %2.4f"%(days))

convtday()