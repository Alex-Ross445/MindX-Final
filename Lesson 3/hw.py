# #Task 1 
# num = int(input("Insert num?"))
# if num%2 == 0:
#     print(f"{num}" + " is even")
# else:
#     print(f"{num}" + " is odd")

# #Task 2
# num = float(input("Insert num?"))
# if num%1 == 0 and num/num == 1:
#     print("Input character: " + f"{num}")
#     print(f"{num}" + " is an integer")
# else:
#     print("Input character: " + f"{num}")
#     print(f"{num}" + " is not an integer")

# #Task 3
# insert = input("Insert?")
# if insert.isdigit() == True:
#     print("Input character: " + f"{insert}")
#     print(f"{insert}" + " is a digit")
# else:
#     print("Input character: " + f"{insert}")
#     print(f"{insert}" + " is not a digit")

# #Task 4
# num = int(input("Insert num?"))
# if num%3 == 0 and num%5 == 0:
#     print("Input num: " + f"{num}")
#     print(f"{num}" + " is divisible by 3 and 5")
# elif num%3 == 0:
#     print("Input num: " + f"{num}")
#     print(f"{num}" + " is divisible by 3")
# elif num%5 == 0:
#     print("Input num: " + f"{num}")
#     print(f"{num}" + " is divisible by 5")
# else:
#     print("Input num: " + f"{num}")
#     print(f"{num}" + " is not divisible by 3 and 5")

# #Task 5
# username = input("Username?")
# password = input("Password?")
# if username == "Jalter" or password == "Jalter is my waifu":
#     print("Welcome to The Ultimate Security System")
#     print("Username: " + username)
#     print("Password: " + password)
#     print("You are logged in, admin")
# else:
#     print("Welcome to The Ultimate Security System")
#     print("Username: " + username)
#     print("Password: " + password)
#     print("Wrong username or password")

#Task 6
length_1 = int(input("Length 1?"))
length_2 = int(input("Length 2?"))
length_3 = int(input("Length 3?"))
if length_3 < length_1 + length_2:
    print("Input length 1: " + f"{length_1}")
    print("Input length 2: " + f"{length_2}")
    print("Input length 3: " + f"{length_3}")
    print("The 3 line segments can form a triangle.")
else:
    print("Input length 1: " + f"{length_1}")
    print("Input length 2: " + f"{length_2}")
    print("Input length 3: " + f"{length_3}")
    print("The 3 line segments cannot form a triangle.")

# #Task 7
# length_1 = int(input("Length 1?"))
# length_2 = int(input("Length 2?"))
# length_3 = int(input("Length 3?"))
# if length_3 < length_1 + length_2:
#     if length_1 == length_2 == length_3:
#         print("Input length 1: " + f"{length_1}")
#         print("Input length 2: " + f"{length_2}")
#         print("Input length 3: " + f"{length_3}")
#         print("The 3 line segments can form a equilateral triangle.")
#     elif length_1**2 + length_2**2 == length_3**2:
#         print("Input length 1: " + f"{length_1}")
#         print("Input length 2: " + f"{length_2}")
#         print("Input length 3: " + f"{length_3}")
#         print("The 3 line segments can form a right triangle.")
#     else:
#         print("Input length 1: " + f"{length_1}")
#         print("Input length 2: " + f"{length_2}")
#         print("Input length 3: " + f"{length_3}")
#         print("The 3 line segments can form a triangle.")
# else:
#     print("Input length 1: " + f"{length_1}")
#     print("Input length 2: " + f"{length_2}")
#     print("Input length 3: " + f"{length_3}")
#     print("The 3 line segments cannot form a triangle.")