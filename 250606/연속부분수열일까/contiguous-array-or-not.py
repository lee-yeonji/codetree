n1, n2 = tuple(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
answer = False

# 수열 B가 수열 A의 연속부분수열인지 확인 : ex) A = [1,2,3,4], B = [1,2] => True
for i in range(n1-n2+1):
    # 수열 B가 수열 A의 부분과 순서까지 완전 일치하는 지 확인
    if a[i:i+len(b)] == b:
        answer = True

# 수열 B가 수열 A의 연속부분수열인지 출력
if answer == True:
    print('Yes')
else:
    print('No')
