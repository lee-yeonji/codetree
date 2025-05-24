n = int(input())

for i in range(1, n+1):
    # 짝수번째 줄 출력
    if i % 2 == 0:
        for _ in range(i):
            print('*', end=' ')
    # 홀수번째 줄 출력 
    else:
        print('*', end=' ')
    print()