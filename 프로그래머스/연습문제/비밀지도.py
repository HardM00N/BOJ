# https://school.programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        or_res = format(arr1[i] | arr2[i], '0{}b'.format(n))
        answer.append(or_res.replace('1', '#').replace('0', ' '))
    
    return answer