class Circle:
    def __init__(self, radius = 2.0, color = "red"):
        self.__radius = radius
        self.__color = color

    def setRadius(self, radius):
        self.__radius = radius

    def setColor(self, color):
        self.__color = color

    def getRadius(self):
        return self.__radius

    def getColor(self):
        return self.__color

    def toString(self):
        return (f"The radius is: {self.getRadius()}" + "\n" + f"The color is: {self.getColor()}")

    def getArea(self):
        return (3.14*(self.getRadius()**2))

class Cylinder(Circle):
    def __init__(self, radius = 2.0, color = "red", height = 1.0):
        super().__init__(radius, color)
        self.__height = height

    def getHeight(self):
        return self.__height

    def setHeight(self, height):
        self.__height = height

    def toString(self):
        return (f"The height is: {self.getHeight()}")

    def getVolume(self):
        return (3.14*(self.getRadius()**2)*self.getHeight())