n = int(input())

for i in range(n):
    for j in range(i, -1, -1):
        if j > i:
            print(" ", end=" ")
        else:
            print(n - j, end=" ")
    print()