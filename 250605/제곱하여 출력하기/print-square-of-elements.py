n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    sqr = arr[i] * arr[i]
    print(sqr, end=' ')