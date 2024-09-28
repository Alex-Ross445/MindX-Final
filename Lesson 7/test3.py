number = [5,1,8,92,-1,30]
num = int(input("Input a number?"))
if num in number == False:
    print("Input a number:" + f"{num}")
    print("Number not found")
else:
    place = number.index(num) + 1
    print("Input a number:" + f"{num}")
    print("Number found at position: " + f"{place}")

print("Sum of all numbers: " + f"{sum(number)}")

print("Input the list of numbers.")
print("Enter 0 to finish.")
new_num = int(input("?"))