import math

#INPUT SECTION
num = int(input("Enter a numerator: Value must be greater than 0: "))
while num < 0:
    num = int(input("Please re-enter the numerator. Value must be greater than 0: "))

denom = int(input("Enter a denominator: Value must be greater than 0: "))
while denom < 0:
    denom = int(input("Please re-enter the numerator. Value must be greater than 0: "))

#PROPER / IMPROPER
if denom > num:
    print(f"{num} / {denom} is a proper fraction.")
    state = "proper fraction"
elif denom <= num:
    print(f"{num} / {denom} is an improper fraction.")
    state = "improper fraction"

#GCD
gcd = math.gcd(num,denom)

numg = num // gcd
denomg = denom // gcd
if gcd==1:
    print(f"This {state} cannot be reduced any further")
else:
    print(f"This {state} can be reduced to {numg} / {denomg}")

