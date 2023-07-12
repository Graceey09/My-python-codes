import random
counter = 1

while counter <= 10:
    random_number = random.randint(1, 10)
    user_number = int(input("Enter number: "))
    if user_number == random_number:
        print("You have won!")
    counter += 1