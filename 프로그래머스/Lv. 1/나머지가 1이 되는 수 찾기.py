# https://school.programmers.co.kr/learn/courses/30/lessons/87389

# 나의 풀이
def solution(n):
    for x in range(1, n + 1):                               # 자연수를 1부터 돌면서
        if n % x == 1:                                      # 나머지가 1이 되는 수를 찾으면 return
            return x
            break

# 다른 사람의 풀이
def solution(n):
    answer = 0

    for divisior in range(2, (n - 1 // 2) + 1) :            # 2부터 ~ 반값까지 
        if (n - 1) % divisior == 0:                         # 약수가 있다면
            answer = divisior 
            break                                           # 탈출
        else: 
            answer = n - 1                                  # 약수가 없다면 본인
    return answer

'''
회고 / TIL
- 쉬운 문제지만, 다른 사람의 풀이를 보면 역시 약수 계산이라 n의 반까지만 계산하고 있음. 
- n의 반까지만 계산하는 스킬을 잘 활용하도록 해야겠음. 
'''