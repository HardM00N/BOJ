# https://school.programmers.co.kr/learn/courses/30/lessons/131701

# 나의 풀이
def solution(elements):
    res = []

    len_elem = len(elements)
    elements = elements + elements                  # 길이 2배로 늘리기 (mod 쓰기 귀찮았...)

    for i in range(1, len_elem + 1):
        for j in range(len_elem):
            res.append(sum(elements[j:j + i]))      # 부분 수열 합 append

    return len(set(res))

# 다른 사람의 풀이
def solution(elements):
    ll = len(elements)
    res = set()                                     # set 선언

    for i in range(ll):
        ssum = elements[i]
        res.add(ssum)
        
        for j in range(i + 1, i + ll):
            ssum += elements[j % ll]                # mod 연산
            res.add(ssum)
    
    return len(res)

'''
회고 / TIL
- 원래 이런 문제 mod 연산으로 푸는데, elements 길이를 단순히 2배하면 구현이 쉬울 것 같아서 그렇게 풀었더니 겁나 느림.
- 다른 사람의 풀이처럼 처음부터 set를 선언하고, mod 연산을 활용한 풀이가 빠름.
'''