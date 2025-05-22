a, b, c = map(int, input().split())

#c의 배수가 없다는 것을 기본으로 설정
satisfied = False

for i in range(a, b+1):
    if i % c == 0:
        satisfied = True

if satisfied == False:
    print('YES')
else:
    print('NO')