# https://school.programmers.co.kr/learn/courses/30/lessons/42889

# 나의 풀이
def solution(N, stages):
    fail_rates = dict()

    for i in range(1, N + 1):                                                       # 각 스테이지를 돌면서
        challenge_cnt = 0                                                           # 해당 스테이지에 도전한 사람 수
        not_clear_cnt = 0                                                           # 해당 스테이지에서 막힌 사람 수
        
        for stage in stages:
            if stage == i:
                not_clear_cnt += 1
            if stage >= i:
                challenge_cnt += 1
        
        try:
            fail_rates[i] = not_clear_cnt / challenge_cnt                           # 실패율 = 막힌 사람 수 / 도전한 사람 수
        except:                                                                     # zero division error 발생 시 0으로 처리
            fail_rates[i] = 0
    
    return [x[0] for x in sorted(fail_rates.items(), key=lambda x: -x[1])]          # 실패율로 내림차순 정렬 후, 스테이지만 리스트로 리턴

# 다른 사람의 풀이
def solution(N, stages):
    answer = []
    fail = []
    info = [0] * (N + 2)
    
    for stage in stages:                                                            # 여기가 핵심
        info[stage] += 1                                                            # 각 스테이지에 대한 info를 생성 (재배열)
   
    for i in range(N):
        be = sum(info[(i + 1):])                                                    # 슬라이싱으로 계산
        yet = info[i + 1]
        
        if be == 0:
            fail.append((i + 1, 0))
        else:
            fail.append((i + 1, yet / be))
    
    for item in sorted(fail, key=lambda x: -x[1]):
        answer.append(item[0])
    
    return answer

'''
회고 / TIL
- 차근차근 풀면 어렵지 않은 문제임.
- 다른 사람의 풀이를 보니 stages에 대한 데이터를 재배치해서 효율적으로 풀었음.
'''