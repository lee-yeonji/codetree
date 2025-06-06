n1, n2 = tuple(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
answer = False

for i in range(n1):
    for j in range(n2):
        if b[j] == a[i] and b[j-1] == a[i-1]:
            answer = True

# 수열 B가 수열 A의 연속부분수열인지 출력
if answer == True:
    print('Yes')
else:
    print('No')
