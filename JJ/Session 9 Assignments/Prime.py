def primecheck(number):
    if number <= 1:
        return False
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

def emirpCheck(number):
    if not primecheck(number):
        return False
    else:
        global reverse
        reverse = 0
        while number != 0:
            sisa = number % 10
            reverse = reverse * 10 + sisa
            number = number//10
        return primecheck(reverse)

number = int(input("Enter any number: "))
if number == 11:
    print("False!")
else:
    a = emirpCheck(number)
    if a == True:
        print(number, reverse)
    else:
        print("False!")