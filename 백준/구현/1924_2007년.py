# https://www.acmicpc.net/problem/1924

# 나의 풀이 (Python3 64ms)
import datetime

x, y = map(int, input().split())

weeks = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
print(weeks[datetime.date(2007, x, y).weekday()])               # 요일 반환 인덱싱

'''
회고 / TIL
- datetime으로 풀었지만 해당 일까지의 일수를 계산해 7로 나눠 요일을 계산하는 것이 정석임.
'''