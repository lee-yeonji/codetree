a, b = map(int, input().split())
# arr = 나머지 0~9 : 크기가 10인 배열
arr = [0] * 10
cnt = 0

while a > 1:
    arr[a % b] += 1
    a //= b

# 나머지가 나온 횟수
for elem in arr:
    cnt += elem ** 2

print(cnt)