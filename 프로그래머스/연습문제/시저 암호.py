# https://school.programmers.co.kr/learn/courses/30/lessons/12926

# 나의 풀이
def solution(s, n):
    words = list(s.split(' '))
    new_words = []

    for word in words:
        new_word = ''

        for ch in word:
            if ch.isupper():                                # 대문자인 경우
                if ord(ch) + n > 90:                        # Z를 넘어갈 경우
                    new_word += chr(ord(ch) + n - 26)
                else:
                    new_word += chr(ord(ch) + n)
            
            else:                                           # 소문자인 경우
                if ord(ch) + n > 122 :                      # z를 넘어갈 경우
                    new_word += chr(ord(ch) + n - 26)
                else:    
                    new_word += chr(ord(ch) + n)

        new_words.append(new_word)
            
    return ' '.join(new_words)

# 다른 사람의 풀이
def caesar(s, n):
    s = list(s)
    
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))

    return "".join(s)

'''
회고 / TIL
- 겁나 무식하게 풀었음.
- % 연산으로 범위를 국한할 수 있는데도 무식하게 풀었음....
'''