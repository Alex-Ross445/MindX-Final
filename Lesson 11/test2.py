shop = {
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30,
    "TOSHIBA" : 10
}
print(shop)

newBrand = input("Input a new brand?")
newNum = int(input("Input the number?"))
newShop = {newBrand: f"{newNum}"}
shop.update(newShop)
print("Available products:")
print(shop)

shop.update({"DELL": 60, "MACBOOK": 2})
print(shop)