n = int(input())
cnt = 1

for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            print(cnt, end=' ')
            cnt += 1
    else:
        for j in range(n):
            print(cnt + (n - 1) - 2 * j, end=' ')
            cnt += 1
    print()