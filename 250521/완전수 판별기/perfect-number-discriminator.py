n = int(input())
sum_val = 0

# 1부터 n-1까지의 수 중에서 약수를 찾는다.
for i in range(1, n):
    if n % i == 0:
        sum_val += i

# sum_val과 n이 같으면 P, 다르면 N을 출력한다.
if sum_val == n:
    print('P')
else:
    print('N')