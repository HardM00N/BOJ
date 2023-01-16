# https://school.programmers.co.kr/learn/courses/30/lessons/67256

# 나의 풀이
def solution(numbers, hand):
    answer = ''
    l, r = 0, 0
    l_mid, r_mid = False, False

    for n in numbers:
        if n == 1:
            answer += 'L'
            l = 3
            l_mid = False
        elif n == 4:
            answer += 'L'
            l = 2
            l_mid = False
        elif n == 7:
            answer += 'L'
            l = 1
            l_mid = False       
        elif n == 3:
            answer += 'R'
            r = 3
            r_mid = False
        elif n == 6:
            answer += 'R'
            r = 2
            r_mid = False
        elif n == 9:
            answer += 'R'
            r = 1
            r_mid = False
        elif n == 2:
            if l_mid and r_mid:
                if l == r:
                    if hand == 'right':
                        answer += 'R'
                        r = 3
                    else:
                        answer += 'L'
                        l = 3
                elif l > r:
                    answer += 'L'
                    l = 3
                else:
                    answer += 'R'
                    r = 3
            elif l_mid and not r_mid:
                if abs(3 - l) == abs(3 - r) + 1:
                    if hand == 'right':
                        answer += 'R'
                        r = 3
                        r_mid = True
                    else:
                        answer += 'L'
                        l = 3
                elif abs(3 - l) < abs(3 - r) + 1:
                    answer += 'L'
                    l = 3
                else:
                    answer += 'R'
                    r = 3
                    r_mid = True
            elif not l_mid and r_mid:
                if abs(3 - l) + 1 == abs(3 - r):
                    if hand == 'right':
                        answer += 'R'
                        r = 3
                    else:
                        answer += 'L'
                        l = 3
                        l_mid = True
                elif abs(3 - l) + 1 > abs(3 - r):
                    answer += 'R'
                    r = 3
                else:
                    answer += 'L'
                    l = 3
                    l_mid = True
            elif not l_mid and not r_mid:
                if l == r:
                    if hand == 'right':
                        answer += 'R'
                        r = 3
                        r_mid = True
                    else:
                        answer += 'L'
                        l = 3
                        l_mid = True
                elif l > r:
                    answer += 'L'
                    l = 3
                    l_mid = True
                else:
                    answer += 'R'
                    r = 3
                    r_mid = True
        elif n == 5:
            if l_mid and r_mid:
                if abs(2 - l) == abs(2 - r):
                    if hand == 'right':
                        answer += 'R'
                        r = 2
                    else:
                        answer += 'L'
                        l = 2
                elif abs(2 - l) < abs(2 - r):
                    answer += 'L'
                    l = 2
                else:
                    answer += 'R'
                    r = 2
            elif l_mid and not r_mid:
                if abs(2 - l) == abs(2 - r) + 1:
                    if hand == 'right':
                        answer += 'R'
                        r = 2
                        r_mid = True
                    else:
                        answer += 'L'
                        l = 2
                elif abs(2 - l) < abs(2 - r) + 1:
                    answer += 'L'
                    l = 2
                else:
                    answer += 'R'
                    r = 2
                    r_mid = True
            elif not l_mid and r_mid:
                if abs(2 - l) + 1 == abs(2 - r):
                    if hand == 'right':
                        answer += 'R'
                        r = 2
                    else:
                        answer += 'L'
                        l = 2
                        l_mid = True
                elif abs(2 - l) + 1 > abs(2 - r):
                    answer += 'R'
                    r = 2
                else:
                    answer += 'L'
                    l = 2
                    l_mid = True
            elif not l_mid and not r_mid:
                if abs(2 - l) == abs(2 - r):
                    if hand == 'right':
                        answer += 'R'
                        r = 2
                        r_mid = True
                    else:
                        answer += 'L'
                        l = 2
                        l_mid = True
                elif abs(2 - l) < abs(2 - r):
                    answer += 'L'
                    l = 2
                    l_mid = True
                else:
                    answer += 'R'
                    r = 2
                    r_mid = True
        elif n == 8:
            if l_mid and r_mid:
                if abs(1 - l) == abs(1 - r):
                    if hand == 'right':
                        answer += 'R'
                        r = 1
                    else:
                        answer += 'L'
                        l = 1
                elif abs(1 - l) < abs(1 - r):
                    answer += 'L'
                    l = 1
                else:
                    answer += 'R'
                    r = 1
            elif l_mid and not r_mid:
                if abs(1 - l) == abs(1 - r) + 1:
                    if hand == 'right':
                        answer += 'R'
                        r = 1
                        r_mid = True
                    else:
                        answer += 'L'
                        l = 1
                elif abs(1 - l) < abs(1 - r) + 1:
                    answer += 'L'
                    l = 1
                else:
                    answer += 'R'
                    r = 1
                    r_mid = True
            elif not l_mid and r_mid:
                if abs(1 - l) + 1 == abs(1 - r):
                    if hand == 'right':
                        answer += 'R'
                        r = 1
                    else:
                        answer += 'L'
                        l = 1
                        l_mid = True
                elif abs(1 - l) + 1 > abs(1 - r):
                    answer += 'R'
                    r = 1
                else:
                    answer += 'L'
                    l = 1
                    l_mid = True
            elif not l_mid and not r_mid:
                if abs(1 - l) == abs(1 - r):
                    if hand == 'right':
                        answer += 'R'
                        r = 1
                        r_mid = True
                    else:
                        answer += 'L'
                        l = 1
                        l_mid = True
                elif abs(1 - l) < abs(1 - r):
                    answer += 'L'
                    l = 1
                    l_mid = True
                else:
                    answer += 'R'
                    r = 1
                    r_mid = True
        elif n == 0:
            if l_mid and r_mid:
                if l == r:
                    if hand == 'right':
                        answer += 'R'
                        r = 0
                    else:
                        answer += 'L'
                        l = 0
                elif l < r:
                    answer += 'L'
                    l = 0
                else:
                    answer += 'R'
                    r = 0
            elif l_mid and not r_mid:
                if l == r + 1:
                    if hand == 'right':
                        answer += 'R'
                        r = 0
                        r_mid = True
                    else:
                        answer += 'L'
                        l = 0
                elif l < r + 1:
                    answer += 'L'
                    l = 0
                else:
                    answer += 'R'
                    r = 0
                    r_mid = True
            elif not l_mid and r_mid:
                if l + 1 == r:
                    if hand == 'right':
                        answer += 'R'
                        r = 0
                    else:
                        answer += 'L'
                        l = 0
                        l_mid = True
                elif l + 1 > r:
                    answer += 'R'
                    r = 0
                else:
                    answer += 'L'
                    l = 0
                    l_mid = True
            elif not l_mid and not r_mid:
                if l == r:
                    if hand == 'right':
                        answer += 'R'
                        r = 0
                        r_mid = True
                    else:
                        answer += 'L'
                        l = 0
                        l_mid = True
                elif l < r:
                    answer += 'L'
                    l = 0
                    l_mid = True
                else:
                    answer += 'R'
                    r = 0
                    r_mid = True

    return answer

'''
회고 / TIL
- 노가다로 한 줄로 펼쳐서 풀었음.
- 시간 효율성은 좋을 것 같음.
- 작성하는 사람은 안 좋음.
'''