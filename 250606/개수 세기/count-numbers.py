n, m = map(int, input().split())
arr = map(int, input().split())

cnt = 0
for i in arr:
    if i == m:
        cnt += 1
print(cnt)