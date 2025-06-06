n = int(input())
nums = list(map(int, input().split()))
sub = []

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if nums[i] > nums[j]:
            sub.append(nums[i] - nums[j])
        else:
            sub.append(nums[j] - nums[i])

print(min(sub))