password = input("Enter a password: ")
while len(password) < 8:
    password = input("Enter a password: ")
print("Your password is secure, and the length is", len(password))