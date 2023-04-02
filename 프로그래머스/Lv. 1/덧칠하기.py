# https://school.programmers.co.kr/learn/courses/30/lessons/161989

# 첫 번째 풀이 (시간 초과)
def solution(n, m, section):
    cnt = 0
    wall = [0] * (n + 1)

    for s in section:
        wall[s] = 1
    
    for s in section:
        wall[s:s + m] = [0] * m
        cnt += 1

        if not sum(wall):
            break

    return cnt

# 두 번째 풀이
def solution(n, m, section):
    cnt = 0
    wall = [0] * (n + 1)

    for s in section:
        wall[s] = 1
    
    for s in section:
        wall[s:s + m] = [0] * m
        cnt += 1

        if not sum(wall):
            break

    return cnt

print(solution(8, 4, [2, 3, 6]))
print(solution(5, 4, [1, 3]))
print(solution(4, 1, [1, 2, 3, 4]))