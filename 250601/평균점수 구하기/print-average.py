arr = list(map(float, input().split()))

sum_val = sum(arr)
num = len(arr)
avg = round(sum_val / num, 1)

print(avg)