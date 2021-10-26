def calcwop(weight, gravity=23.1):
    g = 9.8
    mass = weight/g
    weight2 = mass * gravity
    print(weight2)

calcwop(120,9.8)
calcwop(120)
calcwop(120,23.1)