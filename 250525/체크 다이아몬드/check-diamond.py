n = int(input())

# 위쪽 모양 출력
for i in range(n):
    for _ in range(n - i - 1):
        print(' ', end='')
    for _ in range(i + 1):
        print('* ', end='')
    print()

# 아래쪽 모양 출력
for i in range(n-2, -1, -1):
    for _ in range(n - i - 1):
        print(' ', end='')
    for _ in range(i + 1):
        print('* ', end='')
    print()