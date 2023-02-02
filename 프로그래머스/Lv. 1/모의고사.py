# https://school.programmers.co.kr/learn/courses/30/lessons/42840

# 나의 풀이
def solution(answers):

    answer1 = [1, 2, 3, 4, 5] * 2000                    # 리스트 미리 10000까지 선언
    answer2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    answer3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    
    cnts = [0, 0, 0]
    winners = []

    for i in range(len(answers)):
        
        if answers[i] == answer1[i]:
            cnts[0] += 1
        
        if answers[i] == answer2[i]:
            cnts[1] += 1
        
        if answers[i] == answer3[i]:
            cnts[2] += 1

    max_cnt = max(cnts)                                 # 최다 정답 수 계산

    for i, cnt in enumerate(cnts):                      # 최다 정답 수인 사람 winners에 append
        if cnt == max_cnt:
            winners.append(i + 1)
    
    return sorted(winners)                              # 정렬해서 출력

'''
회고 / TIL
- 다른 사람의 풀이는 비슷해서 생략함.
'''