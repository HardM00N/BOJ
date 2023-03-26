# https://school.programmers.co.kr/learn/courses/30/lessons/17687

# 나의 풀이
def convert(num, base):                             # 재귀적으로 n진수 변환
    temp = '0123456789ABCDEF'
    q, r = divmod(num, base)

    if q == 0:
        return temp[r]
    else:
        return convert(q, base) + temp[r]

def solution(n, t, m, p):
    n_list = ''
    res = ''
    
    for i in range(t * m):                          # t * m만큼 모든 숫자 리스트 생성
        n_list += convert(i, n)

    for i in range(t):
        res += n_list[(p - 1) + m * i]              # 튜브의 순서에 해당하는 인덱스만 res에 추가

    return res

'''
회고 / TIL
- 재귀적 진법 변환 부분은 10 ~ 16진법 사이의 진법들에 대한 방법을 찾다가 검색해서 적용함. 외워두자.
- 문제의 핵심은 진법 변환이고, 나머지는 모든 정답지를 만든 뒤 튜브의 순서에 해당하는 인덱스의 값만 추출하면 됨.
'''