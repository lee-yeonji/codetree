n = int(input())
cnt = ord('A') # ord('A') = 65

for i in range(n):
    for j in range(n):
        print(chr(cnt), end='')
        cnt += 1
    print()