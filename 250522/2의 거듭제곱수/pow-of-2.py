'''n = int(input())
cnt = 0

while n!=1:
    if n % 2 == 1:
        break
    n //= 2
    cnt += 1

print(cnt)'''

# 모범답안
n = int(input())
prod = 1
x = 0

while True:
    #prod가 n이 될 때까지 2를 곱한다.
    if n == prod:
        break
    
    prod *= 2
    x += 1

print(x)