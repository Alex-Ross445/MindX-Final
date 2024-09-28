# print(list(range(5 , 20 , 1))) #start, stop, step
# for val in range(5):
#     print(val)
# for val in "sdjflsjflsjfajf":
#     print(val)

# import turtle
#     turtle.right(72)
#     turtle.forward(200)
# for turtle in range():
#     turtle.left(216)
#     turtle.forward(200)
#     turtle.mainloop() later

# num = 1234578
# while num > 10:
#     print(num)
#     num = num - 10

# while num>0:
#     last_digit = num % 10
#     remain = num // 10
#     num = remain
#     print(last_digit)
#     print(remain)

# for : duyệt các phần tử trong 1 chuỗi; bt trc số lần lặp (Cdài chuỗi)
# while : thực thi các khối lệnh khi điều kiện đc thoả mãn
# while không yêu cầu bt trc số lần lặp

# for i in range(1000):
#     print(i)

#     if i > 100:
#         break

# for i in range(20):
#     if i > 8 and i < 15:
#         continue

#     print(i)

a = 0
b = 1
for val in range(20):
    val = a + b
    a = b
    b = val
    # if val < 20 or val > 100:
    #     continue
    print(val)

# val = a + b
# while val > 0:
#     val = a + b
#     a = b
#     b = val
#     if val > 20 and val < 100:
#         print(val)