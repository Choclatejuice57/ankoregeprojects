weight = int(input("Enter Weight In Kilograms"))
for a in range(1, 16):
    moonweight = weight * 0.165
    weight = weight + 1
    print(weight, "Kilograms On Earth After",a,"Years")
    print(moonweight,"Kilograms On Moon After",a,"Years")
