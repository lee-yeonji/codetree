arr = list(map(int, input().split()))

arr_odd = arr[::2]
arr_even = arr[1::2]

sum_odd = sum(arr_odd)
sum_even = sum(arr_even)

if sum_odd > sum_even:
    print(sum_odd - sum_even)

elif sum_even > sum_odd:
    print(sum_even - sum_odd)

else:
    print(0)