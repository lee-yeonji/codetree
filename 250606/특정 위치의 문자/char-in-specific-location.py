word = ['L', 'E', 'B', 'R', 'O', 'S']

# 찾는 문자 입력
word_ex = input()

# 해당 문자가 리스트에 없는 경우
if word_ex not in word:
    print('None')
# 해당 문자가 리스트에 있는 경우
else:
    print(word.index(word_ex))

'''
other case
# 해당 문자를 찾지 못한 경우
idx = -1

# 문자 탐색: 리스트 내의 원소와 index가 동시에 필요한 경우
for i, char in enumerate(word):
    if char == word_ex:
        idx = i

# 문자가 존재하지 않는 경우
if idx == -1:
    print('None')
else:
    print(idx)
'''