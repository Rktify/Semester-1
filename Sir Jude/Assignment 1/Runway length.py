v = eval(input("Enter the plane's take-off speed in m/s: "))
a = eval(input("Enter the plane's acceleration in m/s**2: "))

length = v**2/(2*a)

print(f"By knowing the take-off speed is {v} m/s and the acceleration is {a} m/s**2. The minimum length of the runway should be %2.4f" % (length))