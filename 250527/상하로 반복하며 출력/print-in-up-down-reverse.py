n = int(input())

for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            if j % 2 == 0:
                print(i+1, end='')
            else:
                print(n-i, end='')
    else:
        for j in range(n):
            if j % 2 == 0:
                print(i+1, end='')
            else:
                print(n-i, end='')
    print()