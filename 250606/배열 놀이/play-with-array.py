n, q = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(q):
    question = list(map(int, input().split()))
    # "1 a" : a번째 원소 출력
    if question[0] == 1:
        value = question[1]
        print(arr[value - 1])
    # "2 b" : N 개의 원소 중에 값이 b인 원소를 찾아, 그 원소가 몇 번째 원소인지 출력
    elif question[0] == 2:
        value = question[1]
        if value in arr:
            print(arr.index(value) + 1)
        else:
            print(0)
    # "3 s e" : s번째 원소부터 e번째 원소까지 각 원소의 값을 공백으로 구분하여 차례대로 출력
    elif question[0] == 3:
        print(*arr[question[1]-1 : question[2]])