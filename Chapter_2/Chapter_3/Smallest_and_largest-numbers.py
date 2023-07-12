counter = 1
total = 0
smallest_number = 0
largest_number = 0
product = 0
while counter <= 4:
    number = int(input('Enter a number: '))
    total = total + number

    average = total / counter

    product = number * number * number * number

    counter = counter + 1

    if number > largest_number:
        largest_number = number

    if number < smallest_number:
        smallest_number = number

print(f"""
sum is: {total}
average is: {average}
product is: {product}
smallest number is: {smallest_number}
largest number is: {largest_number}
""")

