# https://school.programmers.co.kr/learn/courses/30/lessons/12901

# 나의 풀이
import datetime

def solution(a, b):
    day = datetime.datetime(2016, a, b).weekday()                   # datetime의 weekday 활용

    if day == 0:
        return "MON"
    elif day == 1:
        return "TUE"
    elif day == 2:
        return "WED"
    elif day == 3:
        return "THU"
    elif day == 4:
        return "FRI"
    elif day == 5:
        return "SAT"
    else:
        return "SUN"

# 다른 사람의 풀이
def getDayName(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]       # 일수를 계산해 요일 반환
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']        # 리스트를 잘 활용함
    return days[(sum(months[:a - 1])+b - 1) % 7]

'''
회고 / TIL
- 일수를 직접 계산하는 방법부터 datetime을 활용하는 풀이까지 풀이 방법이 다양함.
- datetime.weekday() 정도는 기억하자.
'''