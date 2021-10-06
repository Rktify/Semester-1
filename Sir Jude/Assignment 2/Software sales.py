
p = 99
q = eval(input("Enter the number of packages purchased: "))
if q < 10:
    d = 0
elif q >= 10 and q <= 19:
    d = 10
elif q >= 20 and q <= 49:
    d = 20
elif q >= 50 and q <= 99:
    d = 30
elif q >= 100:
    d = 40

pack = q*p
if d == 0:
    disc = 0
else:
    disc = (d/100)*pack

total = pack - disc
print("Discount amount @ ",d,"% : ${:,.2f}".format(disc))
print("Total amount : ${:,.2f}".format(total))