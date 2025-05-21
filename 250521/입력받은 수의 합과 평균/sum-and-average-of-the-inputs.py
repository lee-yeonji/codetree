n = int(input())
sum_val = 0
avg = 0

for i in range(n):
    a = int(input())
    sum_val += a
avg = round(sum_val / n, 1)
print(sum_val, avg)