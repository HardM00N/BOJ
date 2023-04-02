# https://school.programmers.co.kr/learn/courses/30/lessons/92341

# 나의 풀이
import math
from datetime import datetime

def solution(fees, records):
    res = []
    use_dict, gap_dict = {}, {}
    
    for record in records:                                              # 하루 입출차 기록을 토대로 요금 계산
        time, number, action = record.split()
        
        if action == 'IN':                                              # 입차인 경우
            use_dict[number] = time
        else:                                                           # 출차인 경우
            start = datetime.strptime(use_dict[number], '%H:%M')
            end = datetime.strptime(time, '%H:%M')
            gap = math.ceil(((end - start) / 60).seconds)               # 출차 시간 - 입차 시간을 딕셔너리에 누적

            if number in gap_dict:                                      # 들어온 적 있는 차량인 경우
                gap_dict[number] += gap_dict                        
            else:                                                       # 처음 이용한 차량인 경우
                gap_dict[number] = gap
            
            del use_dict[number]                                        # 출차했으면 삭제

    if use_dict:                                                        # 아직 남아있는 경우 23:59 출차 처리
        for number, start in use_dict.items():
            start = datetime.strptime(start, '%H:%M')
            end = datetime.strptime('23:59', '%H:%M')
            gap = math.ceil(((end - start) / 60).seconds)

            if number in gap_dict:
                gap_dict[number] += gap
            else:
                gap_dict[number] = gap

    for gap in dict(sorted(gap_dict.items())).values():                 # 번호판 기준으로 오름차순 정렬한 누적 시간 딕셔너리를 토대로 요금 계산
        total = fees[1]                                                 # 기본 요금은 모두 추가
        
        if gap > fees[0]:                                               # 기본 요금 시간 초과 시 추가 요금 계산
            total += math.ceil((gap - fees[0]) / fees[2]) * fees[3]
        
        res.append(total)

    return res

'''
회고 / TIL
- 하루 요금 일괄 정산이므로 차근차근 주차 시간을 누적해뒀다가 한 번에 계산하면 쉽게 풀림.
- datetime의 strptime()은 안 보고 쓸 수 있을 정도로 익혀두자.
'''