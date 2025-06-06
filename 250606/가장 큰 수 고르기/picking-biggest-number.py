import sys # 모듈을 불러오는 역할: sys라는 모듈을 불러오기

arr = list(map(int, input().split()))

max_val = -sys.maxsize # 파이썬 안에서 최소 정수값 설정 (sys.maxsize: 최대 정수값 설정)
for elem in arr:
    if elem > max_val:
        max_val = elem

print(max_val)

'''가장 간단한 출력코드
print(max(arr))'''