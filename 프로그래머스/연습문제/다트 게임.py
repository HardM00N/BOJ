# https://school.programmers.co.kr/learn/courses/30/lessons/17682

# 나의 풀이
def solution(dart):
    
    temp = 0
    result = []                                                     # 각 회차의 점수 기록
    i = 0

    while i != len(dart):                                           # 주어진 문자열 탐색
        if dart[i:i + 2].isdigit():                                 # 점수가 두 자리(10)인 경우
            result.append(temp)                                     # 이전 회차의 최종 점수 result에 기록
            temp = int(dart[i:i + 2])                               # 현재 점수 temp에 저장
            i += 1                                                  # 점수가 두 자리였으므로 다음 글자는 skip

        elif dart[i].isdigit():                                     # 점수가 한 자리인 경우
            result.append(temp)                                     # 이전 회차의 최종 점수 result에 기록
            temp = int(dart[i])                                     # 현재 점수 temp에 저장
        
        elif dart[i] == 'D':                                        # 문자가 D라면 temp 제곱
            temp **= 2
        
        elif dart[i] == 'T':                                        # 문자가 T라면 temp 세제곱
            temp **= 3
        
        elif dart[i] == '*':                                        # 문자가 *라면 temp와 앞 점수(result[-1]) 두 배
            temp *= 2
            result[-1] *= 2
        
        elif dart[i] == '#':                                        # 문자가 #라면 temp에 -1 곱함
            temp *= -1
        
        i += 1

    result.append(temp)                                             # 3회차 최종 점수 result에 기록
    
    return sum(result)                                              # 각 회차의 점수 합산

# 다른 사람의 풀이
def solution(dartResult):
    answer = []                                                     # 각 회차의 점수 기록
    
    dartResult = dartResult.replace('10', 'k')                      # 두 자리 점수 k로 대체
    point = ['10' if i == 'k' else i for i in dartResult]           # k를 다시 10으로 바꿔 리스트화

    i = -1
    sdt = ['S', 'D', 'T']
    
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
    
    return sum(answer)


    '''
    회고 / TIL
    - 처음에 10을 간과하고 풀어서 다시 풀었음. 차근차근 구현하면 쉬운 문제임.
    - 다른 사람 풀이 중 정규식을 이용한 부분은 아직 엄두가 안 남... 숙지가 필요함.
    '''