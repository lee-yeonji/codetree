n = int(input())
prod = 1

for i in range(1, n+1):
    prod *= i
    if prod >= n:
        break

print(i)