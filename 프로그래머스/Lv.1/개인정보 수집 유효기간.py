# https://school.programmers.co.kr/learn/courses/30/lessons/150370

# 나의 풀이
import datetime as dt

def solution(today, terms, privacies):
    result = []
    dic_terms = {}

    today = dt.datetime.strptime(today, '%Y.%m.%d')                     # 오늘을 datetime 형식으로 변환

    for term in terms:
        code, month = term.split()
        dic_terms[code] = int(month)                                    # {'A': 6, 'B': 12, 'C': 3} 형태의 딕셔너리 생성

    for i, j in enumerate(privacies):
        start, code = j.split()                                         # privacies를 start와 code로 나눔

        start_date = list(map(int, start.split('.')))
        new_month = start_date[1] + dic_terms[code]                     # 약관 기간을 더해서 새로운 월 도출

        if new_month > 12:                                              # 새로운 월이 12월보다 클 경우 (ex. 15)
            if new_month % 12:
                start_date[0] += new_month // 12                        # 연도를 몫만큼 올려주고 (ex. 15 // 12 = 1)
                start_date[1] = new_month % 12                          # 월은 나머지로 갱신 (ex. 15 % 12 = 3)
            else:                                                       # 새로운 월이 12의 배수일 경우
                start_date[0] += (new_month // 12) - 1                  # 2024년 0월 -> 2023년 12월로 바꿔주는 부분
                start_date[1] = 12                                      # 나머지가 0월이 나오지 않도록 12로 처리
        else:
            start_date[1] = new_month                                   # 새로운 월이 12월보다 작다면 그대로 처리

        expire_date = dt.datetime(*start_date)                          # 만료일자를 datetime 형식으로 변환

        if expire_date <= today:                                        # 만료일자가 오늘보다 이전이었다면
            result.append(i + 1)                                        # 파기할 result에 인덱스 추가

    return sorted(result)

#  다른 사람의 풀이
def to_days(date):                                                      # 날짜를 정수로 변환하는 함수
    year, month, day = map(int, date.split("."))
    return year * 28 * 12 + month * 28 + day

def solution(today, terms, privacies):
    months = {v[0]: int(v[2:]) * 28 for v in terms}                     # terms 딕셔너리로 변환
    today = to_days(today)                                              # 오늘을 정수로 변환
    expire = [
        i + 1 for i, privacy in enumerate(privacies)
        if to_days(privacy[:-2]) + months[privacy[-1]] <= today         # 시작일 + 약관 기간이 오늘보다 이전이라면 인덱스를 expire에 추가
    ]
    return expire
'''
회고 / TIL
- 모든 월이 28일까지만이었기 때문에 일반적인 datetime 연산으로는 풀 수 없지만, 오히려 월만 처리하면 되기에 더 쉽게 풀 수 있음.
- 다른 사람의 풀이는 날짜를 정수로 변환해 정수끼리의 비교로 굉장히 nice하게 풀었음. 좋은 테크닉인 것 같음.
'''