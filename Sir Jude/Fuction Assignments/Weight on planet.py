def calcwop(weight, gravity=23.1): #This function takes 2 arguments, and has a default value for the gravity argument
    g = 9.8
    mass = weight/g
    weight2 = mass * gravity
    print(weight2) #This is the output, I used print cause its easier and faster


#This is how you use the functions, The weight and the gravity respectively
#You can leave the gravity out cause it already has a default value.
calcwop(120,9.8)
calcwop(120)
calcwop(120,23.1)