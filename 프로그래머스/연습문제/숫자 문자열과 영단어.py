# https://school.programmers.co.kr/learn/courses/30/lessons/81301

# 나의 풀이
def solution(s):

    table = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4',     # 표 생성
    'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    
    for key, item in table.items():                                         # 표를 돌면서
        s = s.replace(key, item)                                            # 해당하는 문자열 replace
    
    return int(s)

# 다른 사람의 풀이
def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))                                     # 인덱스로 숫자 대체

    return int(s)

'''
회고 / TIL
- 딕셔너리를 생성해서 반복하면서 문자열을 바꾸도록 풀었음.
- 가장 맨 위에 있는 다른 사람의 풀이가 계속 나랑 똑같아서 신기함...
- 또 다른 풀이 중에 딕셔너리 대신 리스트를 선언하고, 해당하는 숫자의 인덱스를 활용한 경우도 있었음.
'''