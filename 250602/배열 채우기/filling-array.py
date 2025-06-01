arr = list(map(int, input().split()))

# 배열을 뒤집어서 출력
for elem in arr[::-1]:
    if elem == 0:
        continue
    print(elem, end=' ')
