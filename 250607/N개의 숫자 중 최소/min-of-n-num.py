import sys

n = int(input())
a = list(map(int, input().split()))

min_val = sys.maxsize
cnt = 1

for elem in a:
    # 원소가 최솟값보다 작은 경우: 최솟값을 갱신하고 횟수를 1로 초기화
    if min_val > elem:
        min_val = elem
        cnt = 1 # 횟수를 1로 초기화
    elif min_val == elem:
        cnt += 1

print(min_val, cnt)