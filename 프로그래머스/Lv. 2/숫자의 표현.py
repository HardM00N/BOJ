# https://school.programmers.co.kr/learn/courses/30/lessons/12924

# 첫 번째 풀이 (효율성 테스트 시간 초과)
def solution(n):
    cnt = 1

    if n <= 2:
        return cnt

    if n == 3:
        return cnt + 1
    
    search_len = (n + 1) // 2
    search_range = [i + 1 for i in range(search_len)]
    
    for i in range(2, search_len):
        for j in range(0, search_len - i + 1):
            if sum(search_range[j:j + i]) == n:
                cnt += 1
                break

    return cnt

# 두 번째 풀이