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