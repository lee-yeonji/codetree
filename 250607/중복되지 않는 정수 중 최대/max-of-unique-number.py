n = int(input())
nums = list(map(int, input().split()))

max_val = 0
# 중복된 원소들을 모아두는 리스트
new_nums = []

for i in range(n):
    # 특정 원소가 리스트 내 다른 원소와 겹치는 경우: 새로운 리스트에 넣기
    if nums[i] in nums[i+1:]:
        new_nums.append(nums[i])
    # 특정 원소가 새로운 리스트에 있는 경우 (=중복된 원소): 지나가기
    if nums[i] in new_nums:
        continue
    # 리스트 내 중복 원소 제거한 이후, 기존 리스트에서 있는 정수들 중 최댓값 구하기
    if nums[i] > max_val:
        max_val = nums[i]

if max_val == 0:
    print(-1)
else:
    print(max_val)