a, b= map(int, input().split())
arr = [a, b]

for i in range(2, 10):
    # 변수 지정
    num = arr[i-1] + 2 * arr[i - 2]
    # 세 번째 항부터 리스트에 넣기 
    arr.append(num)

print(*arr)