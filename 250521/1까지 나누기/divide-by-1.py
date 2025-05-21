n = int(input())
cnt = 0

for i in range(1, n+1):
    divd = n//i
    n /= i
    # 5,6번 코드를 'n //= i'로 대체 가능 
    cnt += 1
    if divd <= 1:
        break

print(cnt)