n = int(input())
cnt = 0

for i in range(2, n+1):
    divd = n // i
    divd /= i 
    if divd <= 1:
        break
    cnt += 1

print(cnt)