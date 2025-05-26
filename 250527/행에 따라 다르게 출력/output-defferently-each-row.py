n = int(input())
cnt = 0

for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            print(cnt+1, end=' ')
            cnt += 1
    else:
        for j in range(n):
            print(cnt+2, end=' ')
            cnt += 2

    print()