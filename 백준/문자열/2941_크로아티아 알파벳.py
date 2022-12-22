# https://www.acmicpc.net/problem/2941

# 나의 풀이 (Python3 36ms)
word = input()
i, cnt = 0, 0
cro_alpha = set(['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='])

while 1:
    if word[i:i + 2] in cro_alpha:          # 2글자짜리 크로아티아 알파벳
        cnt += 1
        i += 2
    elif word[i:i + 3] in cro_alpha:        # 3글자짜리 크로아티아 알파벳
        cnt += 1
        i += 3
    else:                                   # 아니면 그냥 알파벳
        cnt += 1
        i += 1

    if i >= len(word):
        break
        
print(cnt)

# 다른 사람의 풀이 (Python3 36ms)
word = input()
lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in lst:
    word = word.replace(i, '*')

print(len(word))

'''
회고 / TIL
- 금방 풀었지만 뭔가 무식하게 푼 거 같았는데 다른 사람 풀이를 확인해보니 replace로 깔끔하게 푸셨음.
- replace 잘 활용하면 좋을 것 같음.
'''