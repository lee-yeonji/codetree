arr = list(map(int, input().split()))

for i in range(100, 0, -10):
    cnt = 0
    for elem in arr:
        if elem == 0:
            break
        elif elem - (elem % 10) == i: 
            cnt += 1
    print(f'{i} - {cnt}')