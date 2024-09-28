color = ["blue", "red", "teal", "green"]
read = input("Input position?")
place = color.index(read) + 1
print("Input position: " + f"{place}")
print("Color at position " + f"{place}" + " : " + f"{color[place-1]}")

delete = input("Item to delete?")
location = color.index(delete) + 1
print("Item to delete:" + f"{location}")

import turtle
turtle.pencolor('blue')
turtle.forward(50)
turtle.pencolor('red')
turtle.forward(50)
turtle.pencolor('teal')
turtle.forward(50)
turtle.pencolor('green')
turtle.forward(50)
turtle.mainloop()