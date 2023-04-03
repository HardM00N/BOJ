# https://school.programmers.co.kr/learn/courses/30/lessons/42584

# 나의 풀이
def solution(prices):
    answer = [0] * len(prices)                              # 가격이 떨어지지 않은 기간을 기록할 리스트
    stack = [0]                                             # 가격이 아닌 가격의 인덱스를 저장하는 스택, 첫 요소의 인덱스 넣고 시작

    for i in range(1, len(prices)):                         # 두 번째 요소부터 스택과 비교
        while stack and prices[i] < prices[stack[-1]]:      # 지금 들어온 가격이 스택의 가격보다 낮다면
            idx = stack.pop()                               # 스택에서 낮은 가격들의 인덱스를 계속 pop
            answer[idx] = i - idx                           # 정답지에 현재 인덱스 - 낮은 가격들의 인덱스, 즉 기간을 기록
        
        stack.append(i)                                     # 스택에 남아있는 가격들이 모두 현재 가격보다 낮다면 append

    for i in range(len(answer)):                            # 정답지를 돌면서
        if answer[i] == 0:                                  # 기간이 0인 요소들은 끝까지 가격이 내려가지 않았으므로 
            answer[i] = len(answer) - i - 1                 # 끝까지의 거리를 계산해 정답지에 재기록

    return answer

print(solution([1, 2, 3, 2, 3]))

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.05ms, 10MB)
테스트 3 〉	통과 (0.23ms, 10.1MB)
테스트 4 〉	통과 (0.54ms, 10.1MB)
테스트 5 〉	통과 (0.59ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.32ms, 10.2MB)
테스트 8 〉	통과 (0.37ms, 10.2MB)
테스트 9 〉	통과 (0.04ms, 10.1MB)
테스트 10 〉	통과 (0.62ms, 10.1MB)

효율성  테스트
테스트 1 〉	통과 (27.58ms, 18.8MB)
테스트 2 〉	통과 (21.57ms, 17.6MB)
테스트 3 〉	통과 (32.65ms, 19.5MB)
테스트 4 〉	통과 (23.50ms, 18.3MB)
테스트 5 〉	통과 (16.92ms, 16.9MB)
'''

'''
회고 / TIL
- 1페이지에 있는 다른 사람의 풀이들 중에서 내 코드가 가장 빠름.
- 스택에 가격을 저장하지 않고 가격의 인덱스를 저장해서 기간을 빠르게 계산할 수 있었음.
'''