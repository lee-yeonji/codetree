arr = list(map(int, input().split()))

arr_i = arr[1::2]
arr_j = arr[2::3]

n = len(arr_j)

sum_i = sum(arr_i)
sum_j = sum(arr_j)
avg_j = round(sum_j / n, 1)

print(sum_i, avg_j)