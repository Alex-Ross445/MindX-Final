hero = {
    "Name": "Light",
    "Age": 17,
    "Strength": 8,
    "Defense": 10,
    "HP": 100,
    "Backpack": "Shield, Bread Loaf",
    "Gold": 100,
    "Level": 2
}

newGold = hero["Gold"] + 50
hero.update({"Gold": f"{newGold}"})
print(hero["Gold"])
hero.update({"Backpack": "Shield, Bread Loaf, Flintstone"})
print(hero["Backpack"])