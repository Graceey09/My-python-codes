def times_table(n):
    for a in range(1, 13):
        print()
        for b in range(1, n+1):
            # print(f'{b} x {a} = {a * b:<40}', end="\t\t")
            print("%-3i* %i = %-3i" % (b, a, (a*b)), end="\t\t")


times_table(25)
