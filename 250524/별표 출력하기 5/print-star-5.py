n = int(input())

# i는 각 행마다 *을 몇 묶음씩 출력할 것인지를 의미함
for i in range(n, 0, -1):
    # j는 각 행마다 *묶음을 i번 출력하는 역할을 함 
    for j in range(i):
        # k는 *묶음을 출력해주는 역할 
        for k in range(i):
            print('*', end='')
        print(' ', end='')
    print()