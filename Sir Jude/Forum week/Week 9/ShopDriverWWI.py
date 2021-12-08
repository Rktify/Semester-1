from ShopWWI import ShopWWI

def itemWWI():
    list = [] #This is the list for the items
    num = int(input("Enter the number of items you are going to buy: "))
    while num < 1: #Re-checking if the number entered is at least 1
        print("The number you entered is invalid (Must be at least 1), please retry")
        num = int(input("Enter the number of items you are going to buy:"))
    for i in range(num):
        name = str(input(f"Whats the name of item #{i+1}?: "))
        pound = float(input("How much does the item weight (in pounds)?: "))
        while pound <= 0: #Re-checking if the number entered is lower than 0 or not
            print("The number you entered is invalid (Must be greater than 0), please retry")
            pound = float(input("How much does the item weight (in pounds)?: "))
        print("")
        item = ShopWWI(name,pound)
        list.append(item)
    return list

def showWWI(list):
    print("Items purchased")
    print("---------------------")
    for i in list:
        print(f"Item : {i.getFoodNameWWI()}")
        print(f"Amount : {i.getAmountWWI()} pounds")
        print("Price per pound : ${:.2f}".format(i.getPriceWWI()))
        print("Price of order : ${:.2f}".format(i.PriceCalcWWI()))
        print("")

def priceWWI(list):
    cost = 0
    for i in list:
        cost += i.PriceCalcWWI()
    print("The total cost is: ${:.2f}".format(cost))

def main():
    x = itemWWI()
    showWWI(x)
    priceWWI(x)

main()