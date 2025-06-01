arr = list(map(int, input().split()))
sum_val = 0
cnt = 0

# 10개의 정수 중 250 이상의 수가 나올 때까지의 수의 합계와 개수를 구함
for elem in arr:
    if elem >= 250:
        break
    sum_val += elem
    cnt += 1

avg = sum_val / cnt

print(sum_val, round(avg, 1))
