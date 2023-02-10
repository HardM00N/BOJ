# https://school.programmers.co.kr/learn/courses/30/lessons/12973

import re

def solution(s):
    while s:
        temp = s
        s = re.sub('([a-z])\\2{1,}', '', s)

        if s and temp == s:
            return 0
    else:
        return 1