# https://school.programmers.co.kr/learn/courses/30/lessons/155652

# 나의 풀이
from string import ascii_lowercase

def solution(s, skip, index):
    result = ''

    a_to_z = set(ascii_lowercase)
    a_to_z -= set(skip)                                                     # 차집합
    
    a_to_z = sorted(a_to_z)                                                 # 다시 리스트로 정렬
    l = len(a_to_z)

    dic_alpha = {alpha:idx for idx, alpha in enumerate(a_to_z)}             # 빠른 index 접근을 위한 딕셔너리

    for i in s:
        result += a_to_z[(dic_alpha[i] + index) % l]                        # mod 연산

    return result

'''
테스트 1 〉	통과 (0.02ms, 10.4MB)
테스트 2 〉	통과 (0.01ms, 10.4MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.4MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (0.03ms, 10.4MB)
테스트 14 〉	통과 (0.01ms, 10.3MB)
테스트 15 〉	통과 (0.01ms, 10.3MB)
테스트 16 〉	통과 (0.01ms, 10.3MB)
테스트 17 〉	통과 (0.01ms, 10.5MB)
테스트 18 〉	통과 (0.02ms, 10.3MB)
테스트 19 〉	통과 (0.02ms, 10.4MB)
'''

# 다른 사람의 풀이
def solution(s, skip, index):
    answer = ''
    arr = [chr(i) for i in range(97, 123) if chr(i) not in skip] * 10       # index error 방지

    for i in s:
        answer += arr[arr.index(i) + index]
    
    return answer

'''
테스트 1 〉	통과 (0.05ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.4MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.4MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.02ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10.3MB)
테스트 12 〉	통과 (0.02ms, 10.4MB)
테스트 13 〉	통과 (0.02ms, 10.4MB)
테스트 14 〉	통과 (0.03ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)
테스트 17 〉	통과 (0.01ms, 10.2MB)
테스트 18 〉	통과 (0.02ms, 10.3MB)
테스트 19 〉	통과 (0.02ms, 10.3MB)
'''

'''
회고 / TIL
- 더 쉬운 풀이도 생각났지만 빠른 index() 연산을 위해 딕셔너리를 활용함. 
- 대체적으로 더 빠른 듯?
'''