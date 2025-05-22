satisfied = True
cnt = 0

for _ in range(5):
    n = int(input())
    if n % 3 == 0:
        satisfied = True 
        cnt += 1
    else:
        continue

if cnt < 5:
    print(0)
else:
    print(1)