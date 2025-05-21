n = int(input())
cnt = 0

for i in range(1, n+1):
    divd = n // i
    divd /= i
    cnt += 1
    if divd < 1:
        break

print(cnt)