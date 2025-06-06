nums = list(map(int, input().split()))

value = 500
max_nums = []
min_nums = []

for i in range(10):
    if nums[i] < value:
        min_nums.append(nums[i])
    if nums[i] > value:
        max_nums.append(nums[i])

print(max(min_nums), min(max_nums))