# https://school.programmers.co.kr/learn/courses/30/lessons/12924

# 첫 번째 풀이 (효율성 테스트 시간 초과)
def solution(n):
    cnt = 1                                                 # 자기 자신은 카운트에 포함하고 시작

    if n <= 2:                                              # 2 이하나
        return cnt

    if n == 3:                                                  # 3인 경우 예외 처리
        return cnt + 1
    
    search_len = (n + 1) // 2                                   # 길이를 절반으로 나누고
    search_range = [i + 1 for i in range(search_len)]           # 길이까지의 리스트 생성
    
    for i in range(2, search_len):                              # 구간의 시작점
        for j in range(0, search_len - i + 1):                  # 구간의 길이
            if sum(search_range[j:j + i]) == n:                 # 구간의 합이 n과 같다면
                cnt += 1
                break
            elif sum(search_range[j:j + i]) > n:                # 구간의 합이 n보다 크다면 반복 X
                break

    return cnt

# 두 번째 풀이
def solution(n):
    cnt = 0

    for i in range(1, n + 1):
        total = 0

        for j in range(i, n + 1):
            total += j                                          # 합에 j를 더해나가다가

            if total == n:                                      # n과 같아지면 카운트 & 종료
                cnt += 1
                break
            elif total > n:                                     # n보다 커지면 종료
                break

    return cnt

# 다른 사람의 풀이
def expressions(num):
    return len([i for i in range(1, num + 1, 2) if num % i is 0])

'''
회고 / TIL
- 문제 자체는 쉽지만 첫 번째 풀이의 경우 인덱스와 슬라이싱으로 접근해서 효율성 테스트에서 시간 초과가 발생했음.
- 두 번째 풀이에서는 슬라이싱 대신 그냥 수를 더해가면서 단순 2중 for문으로 푸니 해결됨.
- 다른 사람의 풀이는 제대로 이해하지 못함.
'''