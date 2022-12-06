# https://school.programmers.co.kr/learn/courses/30/lessons/12910

# 나의 풀이
def solution(arr, divisor):
    
    ans = []

    for num in arr:
        if num % divisor == 0:
            ans.append(num)
    if ans:                         # 리스트가 안 비었으면
        return sorted(ans)
    else:                           # 리스트가 비었으면
        return [-1]

# 다른 사람의 풀이
def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]

'''
회고 / TIL
- 프로그래머스에서는 컴프리헨션 고수들이 많다...
'''