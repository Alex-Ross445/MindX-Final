# #Task1
# arr = [0,1,2,3,4,5,6,7,8,9]
# print("Original list:", arr)
# add = [i+2 for i in arr]   
# print("Add 2:", add)
# multi = [i*2 for i in arr]   
# print("Multiply by 2:", multi)
# shift = [arr[i+2] for i in arr]
# print("Shift 2:", shift)

# #Task2
# arr = ['l', 'o', 'o', 'h', 'c', 'S', ' ', 'y', 'g', 'o', 'l',
# 'o', 'n', 'h', 'c', 'e', 'T', ' ', 'X', 'd', 'n', 'i', 'M']
# code = "".join(reversed(arr))
# print(code)

# #Task3
num = int(input("Positive num?"))
while True:
    if num <= 0:
        print("Please input a positive number")
        num = int(input("Positive num?"))
        continue
    else:
        print("Input a positive number: " + f"{num}")
        for val in range(num):
            a = 0
            b = 1
            val = a + b
            b = val
        print("First " + f"{num}" + " Fibonacci number(s):", val)
        break

#Task4
# item = [("Ribeye Steak", 30.5), ("Potato Salad", 5), ("Sparkling Wine", 7), ("Smoked Salmon", 12), ("Chicken Soup", 8.5), ("Tiramisu Cake", 4.5)]