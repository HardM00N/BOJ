# https://school.programmers.co.kr/learn/courses/30/lessons/12930

# 나의 풀이
def solution(s):
    words = list(s.split(' '))                  # 공백을 기준으로 구분
    new_words = []

    for word in words:                          # 구분된 단어들을 돌면서
        new_word = ''
        
        for i, ch in enumerate(word):           # 각 글자의 인덱스로 판별
            if i % 2:
                new_word += ch.lower()
            else:
                new_word += ch.upper()
        
        new_words.append(new_word)
    
    return ' '.join(new_words)                  # 다시 합쳐주기

# print(solution("  tRy hello  WORLD    "))

# 다른 사람의 풀이
def toWeirdCase(s):
    return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split(' ')])

'''
회고 / TIL
- 문제를 잘못 이해해서 푸는데 시간이 좀 걸렸음 (split() -> split(' '))
- 공백이 하나 이상 주어진다길래 split()으로 풀었는데, return할 때 원래의 공백들을 유지해야하므로 split(' ')으로 풀어야 함.
'''