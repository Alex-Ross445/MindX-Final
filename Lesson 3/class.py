a = int(input("Num1?"))
b = int(input("Num2?"))
print("Tổng", a+b)
print("Trừ", a-b)
print("Nhân", a*b)
print("Chia", a/b)
print("Dư", a%b)

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
        int(input("Nhập lại?"))
    else :
        print("Date is 28")
else:
    print("Month non-existence")
    int(input("Nhập lại?"))
    