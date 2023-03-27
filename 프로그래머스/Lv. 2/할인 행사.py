# https://school.programmers.co.kr/learn/courses/30/lessons/131127

# 나의 풀이
from collections import Counter

def solution(want, number, discount):
    want_dict = {}

    for w, n in zip(want, number):                      # 정현이가 원하는 품목의 유사 Counter 딕셔너리 생성
        want_dict[w] = n

    cnt = 0

    for i in range(len(discount) - 9):                  # 10개의 시작점을 한 칸씩 옮기면서
        if want_dict == Counter(discount[i:i + 10]):    # want_dict와 일치하는지 카운트
            cnt += 1

    return cnt

'''
회고 / TIL
- 딕셔너리를 잘 활용하면 쉽게 풀림.
'''