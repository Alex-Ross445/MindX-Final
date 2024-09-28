#Task 1
num = int(input("Num?"))
while True:
    if num > 13:
        print("Input a number: " + f"{num}")
        print("This number is larger than 13")
        break
    elif num == 13:
        print("Input a number: " + f"{num}")
        print("This number is 13")
        break
    else:
        print("Input a number: " + f"{num}")
        print("This number is not larger than 13")
        break

#Task 2
num = int(input("Num?"))
while True:
    if num % 2 == 0:
        print("Input a number: " + f"{num}")
        print("This number is even")
        break
    else:
        print("Input a number: " + f"{num}")
        print("This number is not even")
        break

#Task 3
month = int(input("Month?"))
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 and month >0 and month <13:
    print("Date is 31")
elif month == 4 or month == 6 or month == 9 or month == 11 and month >0 and month <13:
    print("Date is 30")
elif month == 2 and month >0 and month <13:
    a = int(input("Year?"))
    if a %4 ==0 and a >0:
        print("Date is 29")
    elif a <= 0 :
        print("That is BC")
    else :
        print("Date is 28")