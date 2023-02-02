# https://school.programmers.co.kr/learn/courses/30/lessons/12950

# 나의 풀이
def solution(arr1, arr2):
    return [[i + j for i, j in zip(x, y)] for x, y in zip(arr1, arr2)]  # zip을 두 번 활용

# 다른 사람의 풀이
def sumMatrix(A,B):
    return [list(map(sum, zip(*x))) for x in zip(A, B)]                 # *x의 합을 바로 구함 (unpacking)

'''
회고 / TIL
- 앞서 푼 내적 문제와 마찬가지로 zip을 활용해서 풀었음 (1등 풀이와 동일함!)
- 하지만 *x의 합을 바로 구하는 다른 사람의 풀이가 더 좋은 풀이라고 생각됨.
'''