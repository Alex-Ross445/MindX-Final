s = "1326459870"
print(s[0]) #forward
print(s[-3]) #backward
print(s[1:5]) #from a to b
print(s[None:3]) #from extreme to a

name = "Nguyen Minh Tuan"
print(name[-4:None])
print(s[1:6:2]) #cách

name_2 = "Tuan"
age = 22
grettings = "Hello {1} My name is {0}".format(name_2, age)
row1 = "+ {:<15} + {:-^15} + {:->10}".format("Tuan", "Lien", "Loan") #cách vs bn ký tự ở giữa : và <,^,>
print(row1)

row1_1 = "+ {:-<15} + {:-^15} + {:->10}".format("Tuan", "Lien", "Loan")
row2 = "| {:-<15} | {:-^15} | {:->10}".format("x", "y", "z")
row3 = "+ {:-<15} + {:-^15} + {:->10}".format("", "", "")
print(row1_1)
print(row2)
print(row3)

word = input("Type?")
print(len(word))

sbc = int(input("SBC = ?"))
sc = int(input("SC = ?"))
thuong = int(sbc/sc)
sd = sbc - thuong*sc
print(thuong, sd)

# chia lấy nguyên: //
# chia lấy dư: %
# luỹ thừa: **

First = "Tuan"
Middle = "Minh"
Last = "Nguyen"
print(Last + " " + Middle + " " + First)

s1 = "abc"
s2 = "abcdef"
print(s1 < s2)

a = input("Input now")
print(a[::-1])

num1 = 22
num2 = 33
print("Tổng 2 số là" + " " + f"{num1 + num2}")
print("TONG", num1 + num2)

a = input("a?")
b = input("b?")
print(a == b)