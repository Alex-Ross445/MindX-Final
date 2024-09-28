#Task 1
print(list(range(3,12,1)))

#Task 2
num = int(input("Num?"))
print(list(range(0,num+1,1)))

#Task 3
num = int(input("Num?"))
print(list(range(1,num+1,2)))

#Task 4
edge = int(input("Number of edges?"))
import turtle
print("Input number of edges: " + f"{edge}")
for num in range(edge):
    turtle.forward(200)
    turtle.left(180-(1-2/edge)*180)
turtle.mainloop()