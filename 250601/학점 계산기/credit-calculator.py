n = int(input())
arr = list(map(float, input().split()))

sum_val = sum(arr)
avg = round(sum_val / n, 1)

print(avg)

if avg >= 4.0:
    print('Perfect')
elif avg >= 3.0:
    print('Good')
else:
    print('Poor')