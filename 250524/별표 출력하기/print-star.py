n = int(input())

for i in range(n):
    for j in range(i+1):
        print('*', end=' ')
    print()

for i in range(i, -1, -1):
    for j in range(i):
        print('*', end=' ')
    print()