color = ["blue", "red", "teal", "green"]
print("Color list: " + f"{color}")

color.sort()
print("Color list: " + f"{color}")

print("Color list: " + f"{color}")
new_color = input("Input a new color?")
color.append(new_color)
print("New color list: " + f"{color}")