from Cylinderclass import Cylinder

x = Cylinder(1.0, "red", 1.0)
print(f"Radius: {x.getRadius()}")
print(f"Height: {x.getHeight()}")
print(f"Color: {x.getColor()}")
print(f"Area: {'{:.2f}'.format(x.getArea())}")
print(f"Volume: {'{:.2f}'.format(x.getVolume())}")
print()

yn = str(input("Do you want to change the cylinder? (Y/N): "))
print()
if yn == "y" or yn =="Y":
    radius = float(input("Enter the radius: "))
    height = float(input("Enter the height: "))
    color = str(input("Enter the color: "))
    print()
    x.setRadius(radius)
    x.setHeight(height)
    x.setColor(color)
    print(f"Radius: {x.getRadius()}")
    print(f"Height: {x.getHeight()}")
    print(f"Color: {x.getColor()}")
    print(f"Area: {'{:.2f}'.format(x.getArea())}")
    print(f"Volume: {'{:.2f}'.format(x.getVolume())}")
elif yn == "n" or yn =="N":
    print("Well you are kinda boring arent u..? Thats all there is to it.... ty?")
else:
    print("Re-run the program T.T")
    print("I aint loopin this cause u made a typo")


