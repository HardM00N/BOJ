# https://school.programmers.co.kr/learn/courses/30/lessons/161989

# 첫 번째 풀이 (시간 초과)
def solution(n, m, section):
    cnt = 0
    wall = [0] * (n + 1)            # [0, 0, 0, 0]

    for s in section:
        wall[s] = 1                 # [0, 0, 1, 1]
    
    for s in section:
        wall[s:s + m] = [0] * m     # 롤러 길이만큼 칠하기
        cnt += 1

        if not sum(wall):           # 모두 칠해졌다면 합이 0
            break

    return cnt

# 두 번째 풀이
def solution(n, m, section):
    cnt = idx = 0

    for s in section:
        if idx > s:
            continue
        idx = s + m
        cnt += 1

    return cnt

'''
회고 / TIL
- 첫 번째 풀이는 벽을 리스트로 만들어서 다 칠해졌는지를 sum(리스트)로 체크하다보니 시간초과가 발생함.
- 두 번째 풀이는 section을 돌면서 현재 위치가 칠해졌는지, 칠해지지 않았다면 인덱스를 m만큼 더하는 방식으로 산술적으로만 계산함.
- 다른 사람의 풀이는 덱을 사용하는 등 자료구조는 다양하나 풀이 방법은 대체로 같음.
'''