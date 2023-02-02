# https://school.programmers.co.kr/learn/courses/30/lessons/12943

# 나의 풀이
def solution(num):
    
    cnt = 0                                                 # 연산 횟수 카운트
    
    while num != 1:
        cnt += 1    
        
        if num % 2 == 0:                                    # 2로 나누어떨어지면
            num /= 2
        else:
            num = num * 3 + 1

        if cnt >= 500:                                      # 연산횟수가 500번이 넘으면
            return -1                                       # -1 리턴
            break
    
    return cnt                                              # while문이 잘 종료되었으면 cnt 리턴

# 다른 사람의 풀이
def collatz(num):
    for i in range(500):                                    # 500번 제한으로 반복문
        num = num / 2 if num % 2 == 0 else num * 3 + 1      # if문 간결하게...
        if num == 1:
            return i + 1
    return -1

'''
회고 / TIL
- 다른 사람의 풀이를 참고해도 대부분 비슷하게 풀었지만, 컴프리헨션 활용 등의 차이만 있음. 
'''