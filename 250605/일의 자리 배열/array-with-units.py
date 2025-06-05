# 처음 두 수 입력
arr = list(map(int, input().split()))
a = arr

# 앞의 두 수를 더한 값을 원소로 함
for i in range(2, 10):
    a.append((arr[i-2] + arr[i-1]) % 10)
print(*a)
