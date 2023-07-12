def greater(num1, num2, num3, num4):
    maxi = num1
    if num2 > maxi:
        maxi = num2
    if num3 > maxi:
        maxi = num3
    if num4 > maxi:
        maxi = num4
    print("maximum is ", maxi)


greater(100, 1, 9, 250)


# def smaller(number1, number2, number3, number4):
#     smallest_number = number1
#     if number1 < number2:
#         smallest_number = number1
#     if number3 < number2:
#         smallest_number = number3
#     if number4 < number3:
#         smallest_number = number4
#     print('smallest number is ', smallest_number)


# smaller(1, 8, 30, 91)
