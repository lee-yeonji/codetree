n = int(input())
a = list(map(int, input().split()))

new_a = sorted(a, reverse=True)

print(new_a[0], new_a[1])