p = 10
for i in range(p):
    for q in range(i + 1):
        print('*', end=' ')
    for q in range(i, p):
        print(' ', end=' ')
    for q in range(10 - i):
        print("*", end=" ")
    for q in range(i + 1):
        print(" ", end=" ")
    for q in range(i + 1):
        print(" ", end=" ")
    for q in range(10 - i):
        print("*", end=" ")
    for q in range(i + 1):
        print(" ", end=" ")
    for q in range(i + 1):
        print(" ", end=" ")
    for q in range(i, p):
        print(' ', end=' ')
    for q in range(i + 1):
        print('*', end=' ')
    print()
