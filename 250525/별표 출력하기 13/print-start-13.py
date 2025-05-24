n = int(input())

for i in range(2 * n):
    # 홀수 줄 출력
    if i % 2 != 0:
        for _ in range((i//2)+1):
            print('*', end=' ')
    
    # 짝수 줄 출력
    else:
        for _ in range(n-(i//2), 0, -1):
            print('*', end=' ')

    print()