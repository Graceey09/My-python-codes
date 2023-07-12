print("\t\t\tMULTIPLICATION TABLE\n")
for i in range(1, 13):
    print(i, end='\t\t')
print()
print("------------------------------------------------------------------------------------------------\n")
for j in range(1, 13):
    print()
    for k in range(1, 13):
        print(k, "*", j, "=", j * k, end="\t\t")
    print("\n")
