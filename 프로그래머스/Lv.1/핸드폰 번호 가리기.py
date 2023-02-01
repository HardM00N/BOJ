# https://school.programmers.co.kr/learn/courses/30/lessons/12948

# 나의 풀이
def solution(phone_number):
    return '*' * (len(phone_number) - 4) + phone_number[-4:]

# 다른 사람의 풀이 (정규 표현식 활용)
import re

def hide_numbers(s):
    p = re.compile(r'\d(?=\d{4})')
    return p.sub("*", s, count = 0)

'''
회고 / TIL
- 1등 풀이와 똑같아서 기분이 좋음!
- 정규식은 볼 때마다 새로움. 
'''