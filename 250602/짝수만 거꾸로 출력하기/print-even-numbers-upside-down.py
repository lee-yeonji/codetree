n = int(input())

arr = list(map(int, input().split()))

even_arr = []

for elem in arr:
    if elem % 2 == 0:
        even_arr.append(elem)
    
for elem in even_arr[::-1]:
    print(elem, end=' ')