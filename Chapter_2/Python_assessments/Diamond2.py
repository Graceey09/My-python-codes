for a in range(5-2, -1, -1):
    for b in range(5 - a - 1):
        print(" ", end=" ")
    for b in range(2 * a + 1):
        print("*", end=" ")
    print()
