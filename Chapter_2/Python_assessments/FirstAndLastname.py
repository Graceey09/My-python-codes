name = input("Enter your name: ")
if name is None or name == "":
    print("Name cannot be empty")
    exit()

last_name = input("Enter your lastname: ")
if last_name is None or last_name == "":
    print("Name cannot be empty")
    exit()

age = input("Enter your age: ")
age = int(age)
if age < 18:
    print("Your name", "is", name, last_name, "you're underage")
elif age > 65:
    print("Your name", "is", name, last_name, "you're an old Citizen")
elif age < 0:
    print("Your name", "is", name, last_name, "You cannot enter a negative number")
else:
    print("Your name", "is", name, last_name, "and you're a youth")


