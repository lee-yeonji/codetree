n = int(input())

# 시험점수에 따라 등급 결정: 주어지는 점수 n부터 100점까지 1점씩 증가한 점수에 대한 등급 출력
for i in range(n, 101):
    if i >= 90:
        print('A', end=' ')
    elif i >= 80:
        print('B', end=' ')
    elif i >= 70:
        print('C', end=' ')
    elif i >= 60:
        print('D', end=' ')
    else:
        print('F', end=' ')