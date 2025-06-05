A = 0
B = 0
C = 0
D = 0

for i in range(3):
    cold = input().split()
    state = cold[0]
    temp = int(cold[1])
    if state == 'Y':
        if temp >= 37:
            A += 1
        else:
            C += 1

    if state == 'N':
        if temp >= 37:
            B += 1
        else:
            D += 1
    
print(A, B, C, D, end=' ')

if A >= 2:
    print('E')
