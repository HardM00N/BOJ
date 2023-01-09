# https://school.programmers.co.kr/learn/courses/30/lessons/134240

# 나의 풀이
def solution(food):
    left = ''                                           # 왼쪽 음식 배열할 변수

    for i, f in enumerate(food):
        if i == 0:                                      # 물은 무시
            continue
        if f > 1:                                       # 음식의 개수가 1보다 크면
            left += str(i) * (f // 2)                   # 나눈 몫만큼 배열
            
    return left + '0' + left[::-1]                      # 왼쪽 + 0 + 오른쪽

# 다른 사람의 풀이
def solution(food):
    answer = "0"
    
    for i in range(len(food) - 1, 0, -1):
        c = int(food[i] / 2)
        
        while c > 0:
            answer = str(i) + answer + str(i)           # 0을 기준으로 양 옆에 붙여나감
            c -= 1
    
    return answer

'''
회고 / TIL
- 한 쪽만 완성한 후 뒤집으면 쉬움.
- 대체로 풀이가 비슷함.
''' 