n = int(input())
cnt = 1

for i in range(n):
    for j in range(i):
        print(' ', end=' ')
    for j in range(n - i, 0, -1):
        if cnt <= 9:
            print(cnt, end=' ')
            cnt += 1
        elif cnt % 9 == 1:
            print(1, end=' ')
            cnt += 1
        else:
            print(cnt % 9, end=' ')
            cnt += 1
    print()
