n = int(input())
cnt = 2

for i in range(n):
    for j in range(n):
        if cnt <= 8:
            print(cnt, end=' ')
            cnt += 2
        elif cnt % 8 == 0:
            print(8, end=' ')
            cnt += 2
        else:
            print(cnt % 8, end=' ')
            cnt += 2
    print()