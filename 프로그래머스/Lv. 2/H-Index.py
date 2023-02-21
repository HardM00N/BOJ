# https://school.programmers.co.kr/learn/courses/30/lessons/42747

# 나의 풀이
def solution(citations):
    lc = len(citations)
    
    for idx, num in enumerate(sorted(citations)):               # 오름차순 정렬
        if num > lc - (idx + 1):                                # 숫자가 뒤에 남은 수들의 개수보다 크면
            return lc - idx                                     # 전체 길이에서 현재 인덱스르 뺀 값이 정답
    else:                                                       # for문이 return 없이 끝났다면
        return 0                                                # 인용이 없었던 것이므로 0 리턴

# 다른 사람의 풀이 (비슷한 접근법) -> https://ssuamje.tistory.com/47
def solution(citations):
    citations.sort(reverse=True)                                # 내림차순 정렬
    answer = max(map(min, enumerate(citations, start=1)))       # 교차점이 정답
    return answer

'''
회고 / TIL
- 생각보다 쉽게 풀었는데, 질문이나 다른사람풀이 반응들을 보면 다들 어렵게 생각한 것 같음.
- 어쨌거나 로직은 정렬한 리스트를 순회하면서 현재 수와 뒤에 남은 수들의 개수를 비교하는 것임.
- 내림차순으로 푼 다른 사람의 풀이도 상당히 nice함.
'''