# https://school.programmers.co.kr/learn/courses/30/lessons/159994

# 나의 풀이
def solution(cards1, cards2, goal):

    for word in goal:                           # goal에서 한 단어씩 꺼내서
        
        if cards1 and word == cards1[0]:        # cards1이 있다면, cards1의 첫 단어와 비교
            cards1 = cards1[1:]                 # cards1 맨 앞 단어 제거
        
        elif cards2 and word == cards2[0]:      # cards2가 있다면, cards2의 첫 단어와 비교
            cards2 = cards2[1:]                 # cards2 맨 앞 단어 제거
        
        else:
            return "No"                         # 찾는 단어가 cards1, cards2에 없다면
    
    return "Yes"                                # goal의 모든 단어를 다 찾았다면

'''
회고 / TIL
- 레벨 1에 신설된 문제라 풀어봤음. 
- 문자열 비교와 슬라이싱으로 쉽게 풀 수 있었음. 
- 다른 사람의 풀이도 비슷함.
'''