sum_val = 0
avg = 0
cnt = 0

for i in range(10):
    i = int(input())
    if i >= 0 and i <= 200:
        sum_val += i
        cnt += 1

avg = round(sum_val / cnt, 1)
print(sum_val, avg)