# https://school.programmers.co.kr/learn/courses/30/lessons/12911

# 나의 풀이
def solution(n):
    ones = bin(n)[2:].count('1')                # 2진수 변환 후 1의 개수 세기

    while 1:
        n += 1                                  # 1씩 증가시키며 탐색
        new_ones = bin(n)[2:].count('1')

        if ones == new_ones:                    # 1의 개수가 같다면 종료
            break

    return n

'''
회고 / TIL
- 1등 풀이와 비슷한데, 내 코드에서 슬라이싱은 없애도 될 것 같음. (1의 개수를 세는데 영향을 미치지 않기 때문)
'''