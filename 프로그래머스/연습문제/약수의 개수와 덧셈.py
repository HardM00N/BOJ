# https://school.programmers.co.kr/learn/courses/30/lessons/77884

# 나의 풀이
def solution(left, right):
    total = 0
    
    for num in range(left, right + 1):
        divisor_cnt = 1                         # 약수 개수 카운트 (자기자신 포함)
        
        for i in range(1, num // 2 + 1):        # 각 수의 절반까지 돌면서
            if num % i == 0:                    # 약수 찾으면 카운트
                divisor_cnt += 1

        if divisor_cnt % 2:                     # 약수 개수가 홀수면
            total -= num
        else:                                   # 약수 개수가 짝수면
            total += num

    return total

# 다른 사람의 풀이
def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if int(i ** 0.5) == i ** 0.5:           # 제곱근이 정수면, 즉 제곱수면
            answer -= i                         # 약수의 개수는 홀수
        else:
            answer += i
    
    return answer

'''
회고 / TIL
- 굉장히 정직하게 풀었는데, 다른 사람의 풀이를 보니 수학적으로 풀었음. 
- 제곱근이 정수면 약수의 개수가 홀수라는 사실은 처음 알았는데, 잘 숙지했다가 다른 문제에 활용해야겠음.
'''