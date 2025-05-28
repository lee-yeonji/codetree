n = int(input())
cnt = ord('A')

for i in range(n):
    # 빈 칸 출력
    for j in range(i):
        print(' ', end=' ')

    # 알파벳 출력 
    for j in range(n-i):
        print(chr(cnt), end=' ')
        cnt += 1
        if chr(cnt) > 'Z':
            cnt = ord('A')
    print()