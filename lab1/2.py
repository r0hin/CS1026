shopName = input("Enter shop name: ")

ringQTY = int(input("Enter quantity of rings: "))
glassesQTY = int(input("Enter quantity of glasses: "))

print("Shop name: {}".format(shopName))
print("Rings: {}".format(ringQTY))
print("Glasses: {}".format(glassesQTY))

print("Inventory Total: {}".format(ringQTY + glassesQTY))