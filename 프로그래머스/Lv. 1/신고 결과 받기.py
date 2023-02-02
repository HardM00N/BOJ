# https://school.programmers.co.kr/learn/courses/30/lessons/92334

# 나의 풀이
from collections import Counter

def solution(id_list, report, k):
    db = {}

    for id in id_list:                              # 각 유저의 신고 내용을 공집합으로 초기화 (동일 유저의 중복 신고 제거를 위한 set)
        db[id] = set()                              # {'muzi': set(), 'frodo': set(), 'apeach': set(), 'neo': set()}
    
    for r in report:
        name, target = r.split()
        db[name].add(target)                        # {'muzi': {'neo', 'frodo'}, 'frodo': {'neo'}, 'apeach': {'muzi', 'frodo'}, 'neo': set()}

    report_cnt = []                                 # 신고당한 횟수 누적
    
    for id in db.keys():
        if db[id]:
            report_cnt += list(db[id])              # ['neo', 'frodo', 'neo', 'muzi', 'frodo']

    report_cnt = Counter(report_cnt)                # Counter({'frodo': 2, 'neo': 2, 'muzi': 1})
    
    answer = []

    for _, value in db.items():                     # db의 key를 기준으로 돌면서
        cnt = 0
        
        for i in value:                             # value들 중에서
            if report_cnt[i] >= k:                  # 신고당한 횟수가 k 이상인 경우
                cnt += 1                            # 카운트
        
        answer.append(cnt)

    return answer

'''
테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	통과 (0.04ms, 10MB)
테스트 3 〉	통과 (158.72ms, 45.4MB)
테스트 4 〉	통과 (0.08ms, 10.3MB)
테스트 5 〉	통과 (0.08ms, 10.1MB)
테스트 6 〉	통과 (1.56ms, 10.5MB)
테스트 7 〉	통과 (1.91ms, 10.6MB)
테스트 8 〉	통과 (5.46ms, 10.7MB)
테스트 9 〉	통과 (72.01ms, 27.2MB)
테스트 10 〉	통과 (69.13ms, 26.9MB)
테스트 11 〉	통과 (232.78ms, 45.7MB)
테스트 12 〉	통과 (0.27ms, 10.3MB)
테스트 13 〉	통과 (0.26ms, 10.2MB)
테스트 14 〉	통과 (67.46ms, 23.8MB)
테스트 15 〉	통과 (126.43ms, 39MB)
테스트 16 〉	통과 (0.25ms, 10.4MB)
테스트 17 〉	통과 (0.43ms, 10.4MB)
테스트 18 〉	통과 (0.70ms, 10.3MB)
테스트 19 〉	통과 (1.10ms, 10.5MB)
테스트 20 〉	통과 (84.72ms, 23.9MB)
테스트 21 〉	통과 (123.31ms, 39.1MB)
테스트 22 〉	통과 (0.02ms, 10.1MB)
테스트 23 〉	통과 (0.03ms, 10.1MB)
테스트 24 〉	통과 (0.04ms, 10.2MB)
'''

# 다른 사람의 풀이
def solution(id_list, report, k):
    
    answer = [0] * len(id_list)
    dic_report = {id: [] for id in id_list}         # 해당 유저를 신고한 ID
    
    for i in set(report):                           # 중복 제거
        i = i.split()
        dic_report[i[1]].append(i[0])

    for key, value in dic_report.items():
        if len(value) >= k:                         # 신고한 사람들의 수(len(values))를 k와 비교 
            for j in value:
                answer[id_list.index(j)] += 1       # id_list의 순서대로 카운트, 비효율적임

    return answer

'''
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.03ms, 10.2MB)
테스트 3 〉	통과 (1167.78ms, 46.4MB)
테스트 4 〉	통과 (0.05ms, 10.2MB)
테스트 5 〉	통과 (0.03ms, 10.2MB)
테스트 6 〉	통과 (1.16ms, 10.5MB)
테스트 7 〉	통과 (1.61ms, 10.6MB)
테스트 8 〉	통과 (3.86ms, 11.1MB)
테스트 9 〉	통과 (305.39ms, 27.1MB)
테스트 10 〉	통과 (57.82ms, 27.1MB)
테스트 11 〉	통과 (516.76ms, 46.5MB)
테스트 12 〉	통과 (0.46ms, 10.4MB)
테스트 13 〉	통과 (0.19ms, 10.2MB)
테스트 14 〉	통과 (365.22ms, 24.1MB)
테스트 15 〉	통과 (72.92ms, 36.6MB)
테스트 16 〉	통과 (0.26ms, 10.3MB)
테스트 17 〉	통과 (0.20ms, 10.4MB)
테스트 18 〉	통과 (1.21ms, 10.3MB)
테스트 19 〉	통과 (2.26ms, 10.2MB)
테스트 20 〉	통과 (311.30ms, 24.2MB)
테스트 21 〉	통과 (790.77ms, 36.7MB)
테스트 22 〉	통과 (0.01ms, 10.2MB)
테스트 23 〉	통과 (0.01ms, 10.3MB)
테스트 24 〉	통과 (0.01ms, 10.3MB)
'''

'''
회고 / TIL
- 최대한 시간 효율을 생각해서 풀어봤는데, 다른 사람의 풀이들보다 꽤 빨랐음.
- 다른 사람들의 풀이는 신고당한 사람을 기준으로 dic_report를 만들었기 때문에, answer를 도출하는 과정이 비효율적이라 생각됨.
- 나는 신고한 사람의 기준으로 report_cnt를 만들고 Counter를 활용해서 나름 효율적이었던 것 같음.
'''