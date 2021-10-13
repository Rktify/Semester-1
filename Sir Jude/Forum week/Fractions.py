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
if state == "improper fraction":
    gcd = math.gcd(num,denom)
    if gcd==1:
        if num > denom:
            x = num // denom
            y = num % denom
            if y == 0:
                print(f"This {state} cannot be reduced any further")
                print(f"The whole number is {x}")
            else:
                print(f"This {state} cannot be reduced any further")
                print(f"The mixed number is {x} and {y} / {denom}")
        elif num == denom:
            print(f"This {state} can be reduced to 1 / 1")
            print("The whole number is 1")
        else:
            print(f"This {state} cannot be reduced any further")
    else:
        numg = num // gcd
        denomg = denom // gcd
        if numg > denomg:
            x = numg // denomg
            y = numg % denomg
            if y==0:
                print(f"This {state} can be reduced to {numg} / {denomg}")
                print(f"The whole number is {x}")
            else:
                print(f"This {state} can be reduced to {numg} / {denomg}")
                print(f"The mixed number is {x} and {y} / {denomg}")
        elif numg == denomg:
            print(f"This {state} can be reduced to 1 / 1")
            print("The whole number is 1")
        else:
            print(f"This {state} cannot be reduced any further")
else:
    gcd = math.gcd(num,denom)
    if gcd==1:
        pass
    else:
        pass