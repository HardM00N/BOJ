# https://school.programmers.co.kr/learn/courses/30/lessons/17681

# 나의 풀이
def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        or_res = format(arr1[i] | arr2[i], '0{}b'.format(n))            # format(5, '04b') -> '0101'
        answer.append(or_res.replace('1', '#').replace('0', ' '))       # 1과 0을 각각 #과 공백으로 대체
    
    return answer

# 다른 사람의 풀이
def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        a12 = str(bin(i | j)[2:])                                       # '0b'를 없애기 위한 슬라이싱
        a12 = a12.rjust(n, '0')                                         # 오른쪽으로 정렬, 공백을 메울 문자를 입력
        a12 = a12.replace('1', '#')
        a12 = a12.replace('0', ' ')
        answer.append(a12)
    return answer


'''
회고 / TIL
- 카카오 기출문제라 쫄고 시작했지만 문제를 이해하니 간단했음.
- 다른 사람의 풀이를 보니, 내 풀이가 더 나은 것 같음.
- 진법 변환 문제는 재밌는 것 같음.
'''