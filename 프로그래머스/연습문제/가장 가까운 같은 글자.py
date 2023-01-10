# https://school.programmers.co.kr/learn/courses/30/lessons/142086

# 나의 풀이
def solution(s):
    hist = {}                                   # 딕셔너리에 히스토리 기록 (전에 나온 적 있는지)
    res = []                                    # 실제로 리턴할 결과 저장

    for i, ch in enumerate(s):
        if ch in hist:                          # 글자가 나온 적 있으면
            res.append(i - hist[ch][-1])        # 현재의 인덱스 - 해당 글자의 예전 인덱스를 res에 추가
            hist[ch].append(i)                  # 히스토리 최신화
            
        else:                                   # 글자가 나온 적 없으면
            res.append(-1)                      # res에 -1 추가
            hist[ch] = [i]                      # 히스토리에 해당 글자와 인덱스 기록
    
    return res

# 다른 사람의 풀이
def solution(s):
    answer = []
    dic = dict()
    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
        dic[s[i]] = i                           # 해당 글자의 모든 인덱스를 기록하는 대신 최근 인덱스만 기록

    return answer

'''
회고 / TIL
- 대체로 풀이가 비슷함.
- 문자가 나왔다면 그 문자의 마지막 인덱스를 기록해두는 것이 핵심임.
'''