a, b = map(int, input().split())
sum_val = 0

if a > b:
    for i in range(b, a+1):
        if i % 5 == 0:
            sum_val += i
    print(sum_val)

if a < b:
    for i in range(a, b+1):
        if i % 5 == 0:
            sum_val += i 
    print(sum_val)

if a == b:
    if a % 5 == 0:
        sum_val += a
    print(sum_val)