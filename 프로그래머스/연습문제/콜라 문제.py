# https://school.programmers.co.kr/learn/courses/30/lessons/132267

# 나의 풀이
def solution(a, b, n):
    answer = 0

    while n // a:
        new_coke = n // a * b                   # 새로 받을 빈 병
        answer += new_coke                      # total에 더해줌
        n = n % a + new_coke                    # 갖고 있는 빈 병 개수 갱신

    return answer

'''
회고 / TIL
- 다른 사람의 풀이도 대체로 비슷함.
'''