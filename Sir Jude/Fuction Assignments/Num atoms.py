def numatoms(g,w=196.97): #This function is to do the calculations
    avogadro = 6.022*10**23
    atom = (g/w)*avogadro
    return atom #It returns the variable atom back to the a variable


#These 3 are the outputs from the question
#So you do the fucntion, which is numatoms() and you enter the arguments for the amount of element in grams and the weight respectively
a = numatoms(10) #You can leave the weight out since it already has a default weight of 196.97 grs
print(a)
a = numatoms(10,12.001)
print(a)
a = numatoms(10,1.008)
print(a)