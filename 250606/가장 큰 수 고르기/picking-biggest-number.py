import sys

arr = list(map(int, input().split()))

max_val = -sys.maxsize
for elem in arr:
    if elem > max_val:
        max_val = elem

print(max_val)

'''가장 간단한 출력코드
print(max(arr))'''