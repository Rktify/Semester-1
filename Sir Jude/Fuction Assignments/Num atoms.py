def numatoms(g,w=196.97):
    avogadro = 6.022*10**23
    atom = (g/w)*avogadro
    return atom

a = numatoms(10)
print(a)
a = numatoms(10,12.001)
print(a)
a = numatoms(10,1.008)
print(a)