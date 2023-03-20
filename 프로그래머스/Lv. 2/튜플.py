# https://school.programmers.co.kr/learn/courses/30/lessons/64065

# 나의 풀이
import re

def solution(s):
    res = []
    sets = s[2:-1].split(',{')              # 앞 뒤 괄호 제거 후 ,{으로 split
    sets.sort(key=len)                      # 길이 순으로 오름차순 정렬

    for s in sets:
        numbers = re.findall(r'\d+', s)     # 숫자만 추출
        for n in numbers:
            n = int(n)
            if n not in res:                # 아직 res에 없다면 append
                res.append(n)

    return res

# 다른 사람의 풀이
import re
from collections import Counter

def solution(s):

    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

'''
회고 / TIL
- 귤 고르기와 비슷한 문제인 것 같음.
- 다른 사람의 풀이는 단순히 모든 숫자를 추출한 후 빈도 역순으로 나열함. (귤 고르기와 유사)
'''