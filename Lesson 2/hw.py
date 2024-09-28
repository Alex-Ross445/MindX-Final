#Task 1
from cmath import sqrt
import math
radius = int(input("Radius?"))
π = 3.1416
print("Perimeter: " + f"{π * radius * 2}")
print("Area: " + f"{π * radius**2}")

#Task 2
Length_of_edge = int(input("Width?"))
print("Length of diagonal line: " + f"{Length_of_edge*sqrt(2)}")

#Task 3
email = "ttn0957@gmail.com"
print("Account name: " + email[0:7])
print("Domain name: " + email[-10:None])
print("Full email: " + email)

#Task 4
day = input("Day?")
month = input("Month?")
year = input("Year?")
mdy = "Date in MM/DD/YYYY format: {0:0>2}/{1:0>2}/{2:0>4}".format(month,day,year)
dmy = "Date in MM/DD/YYYY format: {0:0>2}/{1:0>2}/{2:0>4}".format(day,month,year)
print(mdy)
print(dmy)

#Task 5
deposit = int(input("Money?"))
rate = int(input("%?"))/100
after = int(input("After year?"))
print("Account after " + f"{after}" + " years: " + f"{deposit*(1+rate)**after}")

#Task6
import math
import turtle
turtle.forward(300)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(300)
turtle.left(90)
turtle.forward(200)
turtle.right(180)
turtle.pensize(5)
turtle.pencolor('#de5246')
turtle.forward(200)
turtle.right(90+33)
turtle.forward(50*math.sqrt(13))
turtle.left(33+33)
turtle.forward(50*math.sqrt(13)-1)
turtle.right(90+33)
turtle.forward(200)
turtle.mainloop()

#Task7
import turtle
turtle.pensize(6)
turtle.pencolor('#cf8f03')
turtle.left(30)
turtle.forward(200)
turtle.right(60)
turtle.forward(200)
turtle.right(120)
turtle.forward(200)
turtle.right(60)
turtle.forward(200)
turtle.right(90+60)
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.pencolor('#0b2c3c')
turtle.left(30)
turtle.forward(200)
turtle.right(60)
turtle.forward(200)
turtle.right(120)
turtle.forward(200)
turtle.right(60)
turtle.forward(200)
turtle.mainloop()