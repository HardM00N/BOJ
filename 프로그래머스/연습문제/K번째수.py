# https://school.programmers.co.kr/learn/courses/30/lessons/42748

# 나의 풀이
def solution(array, commands):
    answer = []
    
    for command in commands:
        new_arr = array[command[0] - 1:command[1]]              # 새로운 리스트로 슬라이싱
        answer.append(sorted(new_arr)[command[2] - 1])          # 새로운 리스트 정렬 후 원하는 인덱스의 값 append
    
    return answer

# 다른 사람의 풀이
def solution(array, commands):
    answer = []
    
    for command in commands:
        i, j ,k = command                                       # 언패킹으로 코드 간결화
        answer.append(sorted(array[i - 1:j])[k - 1])
    
    return answer

'''
회고 / TIL
- 문제 그대로 슬라이싱하고 정렬해 인덱싱하면 쉽게 풀림.
- 다른 사람의 풀이를 보니 i, j, k로 언패킹해 코드를 나보다 간결하게 썼음. 참고하자.
'''