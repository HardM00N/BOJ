# https://school.programmers.co.kr/learn/courses/30/lessons/17684

# 나의 풀이
from string import ascii_uppercase

def solution(msg):
    lzw = {}
    answer = []

    for idx, word in enumerate(ascii_uppercase):        # 알파벳으로 초기화된 딕셔너리 생성
        lzw[word] = idx + 1

    i = 0

    while i < len(msg):                                 # 검색어 시작점

        for j in range(i + 1, len(msg) + 1):            # 검색어 종료점
            if msg[i:j] not in lzw:                     # 검색어가 딕셔너리에 없다면
                answer.append(lzw[msg[i:j - 1]])        # 직전의 검색어의 인덱스를 answer에 추가하고
                lzw[msg[i:j]] = len(lzw) + 1            # 새 검색어를 딕셔너리에 추가
                
                i += len(msg[i:j - 1])                  # 검색어 시작점을 성공한 검색어 길이만큼 옮기기
                break
            else:                                       # 검색어가 딕셔너리에 있는데
                if j == len(msg):                       # 검색어 종료점이 msg의 길이라면, 즉 마지막 검색어라면
                    answer.append(lzw[msg[i:j]])        # answer에 마지막 검색어의 인덱스를 추가하고
                    i += len(msg)                       # while을 탈출하기 위해 i를 크게 만들기

    return answer

'''
회고 / TIL
- 검색에 성공했을 경우 다음 단어부터 검색하도록 인덱스를 잘 설정하면 풀리는 문제
- 풀이법이 워낙 다양하나 대체로 큰 맥락은 비슷함.
'''