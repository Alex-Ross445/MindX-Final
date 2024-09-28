shop = {
    "HP" : 600,
    "DELL" : 650,
    "MACBOOK" : 1200,
    "ASUS" : 400
}

print("Price of ASUS: " + f"{shop['ASUS']}")

brand = input("Input a brand name: ")
print("Price of " + brand + ": " + f"{shop[brand]}")