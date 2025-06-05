# 배열 선언
cnt = 0
arr = []

# 정수 1~10 중 1개 입력받기
n = int(input())

# 입력 받은 정수의 배수를 배열에 입력
for i in range(1, 11):
    arr.append(n*i)
    if (n * i) % 5 == 0:
        cnt += 1
        if cnt == 2:
            break

# 5의 배수가 2번 입력되면 출력 후 종료
print(*arr)

    