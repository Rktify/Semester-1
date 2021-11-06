def output():
    v = Cars.get(i)
    for x in v:
        print("-",x)


Cars = {
    "JJ" : ["Innova", "SubaUwU", "Yaris"],
    "Filbert" : ["Chevrolet", "Ford", "Triumph"],
    "Steph" : ["Mini Cooper", "Camry", "Lexus"],
    "Alvin" : ["Ferrari", "Renault", "Cadillac"],
    "Dio" : ["Pontiac", "Mercedes", "Maserati"]
}


for i in ["JJ", "Filbert", "Steph", "Alvin", "Dio"]:
    print(f"{i} likes these cars :")
    output()
    print()