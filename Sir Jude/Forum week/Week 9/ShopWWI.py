class ShopWWI: #Initializer
    def __init__(self,food,amount):
        self.__food = food
        self.__amount = amount
        self.__price = self.getPriceWWI()
        self.__totalprice = self.PriceCalcWWI()

    def getFoodNameWWI(self): #Get the food names
        return self.__food

    def getAmountWWI(self): #Get the amount
        return self.__amount

    def __PriceListWWI(self): #The price list for each item
        if self.__food == "Dry Cured Iberian Ham":
            self.__price = 177.80
        elif self.__food == "Wagyu Steaks":
            self.__price = 450.00
        elif self.__food == "Matsutake Mushrooms":
            self.__price = 272.00
        elif self.__food == "Kopi Luwak Coffee":
            self.__price = 306.50
        elif self.__food == "Moose Cheese":
            self.__price = 487.20
        elif self.__food == "White Truffles":
            self.__price = 3600.00
        elif self.__food == "Blue Fin Tuna":
            self.__price = 3603.00
        elif self.__food == "Le Bonnotte Potatoes":
            self.__price = 270.81
        else:
            self.__price = 0

    def getPriceWWI(self): #Get the prices
        self.__PriceListWWI()
        return self.__price

    def PriceCalcWWI(self): #To calculate the item price
        self.__totalprice = self.__price * self.__amount
        return self.__totalprice