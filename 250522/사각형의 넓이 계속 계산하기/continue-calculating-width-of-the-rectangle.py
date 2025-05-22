while True:
    letters = input().split()
    a,b = int(letters[0]), int(letters[1])
    c = letters[2]
    
    if letters[2] == 'C':
        print(a*b)
        break
    else:
        print(a*b)