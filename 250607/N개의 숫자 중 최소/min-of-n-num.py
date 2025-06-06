import sys

n = int(input())
a = list(map(int, input().split()))

cnt = 0
min_val = sys.maxsize
for elem in a:
    if min_val > elem:
        min_val = elem
        cnt += 1

print(min_val, cnt)