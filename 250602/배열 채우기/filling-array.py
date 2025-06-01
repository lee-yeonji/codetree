arr = list(map(int, input().split()))
new_arr = []

# 배열에 0이 있는 경우, 0 제거
for elem in arr:
    if elem == 0:
        break
    new_arr.append(elem)

# 배열을 뒤집어서 출력
for i in new_arr[::-1]:
    print(i, end=' ')
