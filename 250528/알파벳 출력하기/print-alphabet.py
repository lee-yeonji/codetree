n = int(input())
cnt = ord('A')

for i in range(n):
    for j in range(i+1):
        print(chr(cnt), end='')
        cnt += 1
        if chr(cnt) > 'Z':
            cnt = ord('A')
    print()