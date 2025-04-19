n = int(input())

for i in range(n):
    # n개의 줄에 걸쳐 정수 입력 
    nn = int(input())
    # 주어진 수 중 홀수이면서 3의 배수인 수들만 순서대로 출력 
    if (nn % 2 != 0) and (nn % 3 == 0):
        print(nn)