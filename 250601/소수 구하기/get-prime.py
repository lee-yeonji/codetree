n = int(input())

for i in range(1, n+1):
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
    
    # 약수의 개수가 2개(1과 자기 자신)일 경우 => 소수
    if cnt == 2:
        print(i, end=' ')