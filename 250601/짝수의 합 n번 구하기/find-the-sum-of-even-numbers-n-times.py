n  = int(input())

for i in range(n):
    a, b = map(int, input().split())
    sum_val = 0
    for j in range(a, b+1):
        if j % 2 == 0:
            sum_val += j
        else:
            continue
    print(sum_val)