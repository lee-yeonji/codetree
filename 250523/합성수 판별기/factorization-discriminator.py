n = int(input())
cv = False

for i in range(2, n):
    if n % i == 0:
        cv = True
        break

if cv == True:
    print('C')
else:
    print('N')