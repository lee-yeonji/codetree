n = int(input())

'''문제 풀이
# 모양에 맞게 윗쪽 별 출력 (역삼각형)
for i in range(n):
    for j in range(i):
        print(' ', end=' ')
    for j in range((2 * n)-(2 * i)-1, 0, -1):
        print('*', end=' ')
    print()

# 모양에 맞게 아랫쪽 별 출력 (정삼각형)
for i in range(n-1):
    for j in range(n-i-2):
        print(' ', end=' ')
    for j in range(2 * (i + 1) + 1):
        print('*', end=' ')
    print()
'''
#모범 답안
for i in range(n):
    for _ in range(i):
        print(' ', end=' ')
    for _ in range((2 * n)-(2 * i)-1):
        print('*', end=' ')
    print()

for i in range(n-2, -1, -1):
    for _ in range(i):
        print(' ', end=' ')
    for _ in range((2 * n) - (2 * i) - 1):
        print('*', end=' ')
    print()