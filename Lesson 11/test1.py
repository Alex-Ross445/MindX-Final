shop = {
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30
}

print("Available MACBOOK: " + f"{shop['MACBOOK']}")

brand = input("Brand name?")
print("Available " + brand + "s: " + f"{shop[brand]}")