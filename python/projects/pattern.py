num = int(input("Enter an integer"))

for i in range(1, num):
    for j in range(1, i + 1):
        print(i, end="")
    print("")
