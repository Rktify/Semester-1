def primecheck(number):
    if number <= 1:
        return False
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

def emirpCheck(number):
    global reverse
    reverse = 0
    if not primecheck(number):
        return False
    else:
        while number != 0:
            sisa = number % 10
            reverse = reverse * 10 + sisa
            number = number//10
        return primecheck(reverse)

number = int(input("Enter any number: "))

a = emirpCheck(number)
if number==reverse:
    print("False!")
elif a == True:
    print(number, reverse)
else:
    print("False!")