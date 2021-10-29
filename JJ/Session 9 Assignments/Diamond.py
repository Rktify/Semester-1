def dia():
    for i in range(height):
        print(" " * (height-i),end="")
        for j in range(i*2+1):
            print("*",end="")
        print()
    for i in range(height-2,-1,-1):
        print(" " * (height-i),end="")
        for j in range(i*2+1):
            print("*",end="")
        print()

height = int(input("How tall do you want this diamond to be?: "))
dia()