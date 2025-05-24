n = int(input())

# i는 행, j는 열을 뜻함

for i in range(2 * n + 1):
    for j in range(2 * n + 1):
        # 홀수 행 출력
        if i % 2 == 0:
            print('*', end=' ')
        # 짝수 행 출력
        else:
            # 짝수 열 출력 (0~)
            if j % 2 == 0:
                print('*', end=' ')
            # 홀수 열 출력 
            else:
                print(' ', end=' ')
    print()