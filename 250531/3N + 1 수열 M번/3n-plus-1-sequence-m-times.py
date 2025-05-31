m = int(input())

for _ in range(m):
    n = int(input())
    # 반복 횟수
    cnt = 0

    # n이 1이 될 때 조건문은 끝남.
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n*3 + 1
        cnt += 1
    print(cnt)