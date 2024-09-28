#Task 1
num = int(input("Num?"))
print("Input number: " + f"{num}")
for a in range(num):
    a = a + 1
    print("#"*a)

#Task 2
num = int(input("Num?"))
while True:
    if num <= 0:
        num = int(input("Num?"))
        continue
    print("Input a positive number: " + f"{num}")
    print("Thank you")
    break

#Task 3
gt = int(input("Giai thừa?"))
while True:
    if gt < 0:
        gt = int(input("Giai thừa?"))
        continue
    if gt == 0:
        print("0! = 1")
        break
    for i in range(1, gt+1):
        break

#Task 4
num = int(input("Num?"))
print("Input number: " + f"{num}")
while True:
    if num < 0:
        num = int(input("Num?"))
        continue
    last_digit = num % 10
    remain = num // 10
    total = last_digit + remain
    print("Sum of digits of " + f"{num}" + " = " + f"{total}")
    break

#Task 5
a = 1
for num in range(10000):
    num = 1000 + a
    a = a + 1
    if num >= 1000 and num <= 9999:
        # total = f"{num[0]}" + f"{num[1]}" + f"{num[2]}" + f"{num[3]}"
        # if total == 9:
            print(total)

# num = 123452
# print(f"{num}"[1])

#Task 6
edge = int(input("Number of edges?"))
from tkinter import mainloop
import turtle
print("Input number of edges: " + f"{edge}")
for num in range(edge):
    turtle.forward(200)
    turtle.left(180-(1-2/edge)*180)
turtle.mainloop()

#Task 7
