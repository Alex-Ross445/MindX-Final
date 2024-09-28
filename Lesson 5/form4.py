#Task 1
username = input("Username?")
password = input("Pass?")
email = input("Email?")
print("== Registration ==")
print("Username: " + username)
print("Password: " + password)
print("Email: " + email)
print("Registered successfully.")

#Task 2
username = input("Username?")
password = input("Pass?")
repass = input("Repeat password:")
email = input("Email?")
print("== Registration ==" + '\n')
print("Username: " + username + '\n')
print("Password: " + password)
while True:
    if password != repass:
        print("Passwords not match. Please input again.")
        repass = input("Repeat password:")
        continue
    else:
        print("Repeat password: "+ repass + '\n')
    break
print("Email: " + email +'\n')
print("Registered successfully.")

#Task 3
username = input("Username?")
password = input("Pass?")
repass = input("Repeat password:")
email = input("Email?")
print("== Registration ==" + '\n')
print("Username: " + username + '\n')
print("Password: " + password)
while True:
    if password != repass:
        print("Passwords not match. Please input again.")
        repass = input("Repeat password:")
        continue
    else:
        print("Repeat password: "+ repass + '\n')
    break
while True:
    if email[-10:None] != "@gmail.com":
        print("Invalid email. Please input again.")
        email = input("Email?")
    else:
        print("Email: " + email + '\n')
        break
print("Registered successfully.")