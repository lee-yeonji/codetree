n = int(input())
cnt = 0

for i in range(1, n+1):
    divd = n//i
    n /= i
    cnt += 1
    if divd <= 1:
        break

print(cnt)