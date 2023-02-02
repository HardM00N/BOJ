# https://school.programmers.co.kr/learn/courses/30/lessons/12916

# 나의 풀이
def solution(s):
    p_cnt, y_cnt = 0, 0

    for i in s:
        if i == 'p' or i == 'P':                            # 문자열에 p나 P가 있으면
            p_cnt += 1
        elif i == 'y' or i == 'Y':                          # 문자열에 y나 Y가 있으면
            y_cnt += 1
    
    if p_cnt == y_cnt:                                      # p와 y의 개수가 같으면
        return True
    else:
        return False

# 다른 사람의 풀이
def numPY(s):
    return s.lower().count('p') == s.lower().count('y')     # 문자열 자체를 소문자로 바꾸고, 소문자만 카운트

'''
회고 / TIL
- 내가 여러 줄로 푼 걸 다른 사람이 한 줄로 쉽게 풀었음...
- 받은 문자열 자체를 소문자로 바꾸면 대문자는 고려하지 않아도 됨... 
- 또한 문자열의 count 메서드를 쓸 수가 있었음...
'''