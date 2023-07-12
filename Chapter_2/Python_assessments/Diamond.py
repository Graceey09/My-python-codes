for a in range(5):
    for c in range(5 - a - 1):
        print(" ", end=" ")
    for c in range(2 * a + 1):
        print("*", end=" ")
    print()

