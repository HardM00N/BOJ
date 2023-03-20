# https://school.programmers.co.kr/learn/courses/30/lessons/17677

# 나의 풀이
def solution(str1, str2):
    str1, str2 = str1.upper(), str2.upper()                                 # 모두 대문자로
    list1, list2 = [], []

    for i in range(len(str1) - 1):
        if str1[i:i + 2].isalpha():                                         # 알파벳 2글자씩만 리스트에 추가
            list1.append(str1[i:i + 2])

    for i in range(len(str2) - 1):
        if str2[i:i + 2].isalpha():                                         # 알파벳 2글자씩만 리스트에 추가
            list2.append(str2[i:i + 2])

    total = set(list1) | set(list2)
    inter, union = [], []

    if total:                                                               # list1, list2 모두 공집합이 아니라면
        for i in total:
            union.extend([i] * max(list1.count(i), list2.count(i)))         # extend로 많은 개수만큼 그대로 합집합에 추가
            inter.extend([i] * min(list1.count(i), list2.count(i)))         # 가장 적은 개수만큼이 교집합

        return int(len(inter) / len(union) * 65536)

    else:
        return 65536
    
# 다른 사람의 풀이 (정규식)
import re
import math

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum) * 65536)

'''
회고 / TIL
- 반가운 자카드 유사도
- 차근차근 구현하면 되는데, 급하게 풀다가 꼬였었음.
- 다른 사람의 풀이는 정규식을 활용하고, 교집합을 구해서 풀었음.
'''