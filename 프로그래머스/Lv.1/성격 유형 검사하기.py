# https://school.programmers.co.kr/learn/courses/30/lessons/118666

# 나의 풀이
def solution(survey, choices):

    result = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for question, score in zip(survey, choices):
        if score == 4:                                                              # 모르겠음인 경우 패스
            continue

        if score < 4:                                                               # 비동의에 가깝다면
            result[question[0]] += 4 - score
        else:                                                                       # 동의에 가깝다면
            result[question[1]] += score % 4

    answer = ''

    if result['R'] >= result['T']:                                                  # 한 지표의 두 점수가 같을 경우는 사전 순
        answer += 'R'
    else:
        answer += 'T'
    if result['C'] >= result['F']:
        answer += 'C'
    else:
        answer += 'F'
    if result['J'] >= result['M']:
        answer += 'J'
    else:
        answer += 'M'
    if result['A'] >= result['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer

# 다른 사람의 풀이
def solution(survey, choices):

    my_dict = {"RT":0,"CF":0,"JM":0,"AN":0}
    
    for A,B in zip(survey,choices):
        if A not in my_dict.keys():
            A = A[::-1]
            my_dict[A] -= B - 4                                                     # 애초에 비동의를 음수로 받음
        else:
            my_dict[A] += B - 4

    result = ""
    
    for name in my_dict.keys():
        if my_dict[name] > 0:
            result += name[1]
        elif my_dict[name] < 0:
            result += name[0]
        else:
            result += sorted(name)[0]

    return result
'''
회고 / TIL
- 문제에 입각해 1~3점으로 받았는데 다른 사람의 풀이를 보니 애초에 비동의를 음수로 받으면 풀이가 더 간결해짐.
- 그 외엔 단순 구현 문제였음.
'''