# https://school.programmers.co.kr/learn/courses/30/lessons/12935

# 나의 풀이
def solution(arr):
    arr.remove(min(arr))
    return arr or [-1]

# 다른 사람의 풀이 (안 좋은 예)
def rm_small(mylist):
    return [i for i in mylist if i > min(mylist)]   # 비효율적인 코드

'''
회고 / TIL
- 최솟값을 제거하고 단순히 리턴함. 
- 다른 사람의 풀이는 간단해 보이지만 min()이 반복적으로 연산되어 비효율적임.
'''