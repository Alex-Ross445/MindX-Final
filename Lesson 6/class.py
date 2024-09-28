# i = list((1,2,3,4,5))
# # có thể lưu các đối tg có kiểu dữ liệu khác nhau
# print(i)
# print(len(i))
# i.append("sjfldsjfl") #nối vào bên phải
# i.insert(1, "jljkj") #nối vào stt
# print(i)

# i = list(range(0,11))
# print(i)

# l = [i for i in range(20,40)]
# l.pop(-1) #delete
# print(l)

# l = [1,2,3,4,5]
# ref = l
# ref[0] = 100
# print(l)

# t = tuple(list(tuple([1,2,3])))
# print(t)

from timeit import timeit


t1 = timeit('[i for i in range(int(1e2))]')
t2 = timeit('(i for i in range(int(1e2)))')

print("List:",t1)
print("Tuple:",t2)
print("Faster than x", t1/t2)