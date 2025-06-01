start, end = map(int, input().split())
cnt = 0

for i in range(start, end+1):
    # n의 진약수의 총 합 = sum_val
    sum_val = 0
    
    for j in range(1, i+1):
        if i % j == 0 and i != j:
            sum_val += j
    if sum_val == i:
        cnt += 1
print(cnt)