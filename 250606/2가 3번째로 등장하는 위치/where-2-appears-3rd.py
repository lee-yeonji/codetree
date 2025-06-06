n = int(input())
arr = list(map(int, input().split()))
cnt = 0

# 리스트 내 원소와 index가 동시에 필요한 경우 => enumerate() 함수 이용
for i, elem in enumerate(arr):
    if elem == 2:
        cnt += 1
        if cnt == 3:
            print(i + 1)