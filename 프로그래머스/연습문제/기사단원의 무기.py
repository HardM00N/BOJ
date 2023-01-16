# https://school.programmers.co.kr/learn/courses/30/lessons/136798

# 나의 풀이
def solution(number, limit, power):
    res = 0
    
    for n in range(1, number + 1):
        if n == 1:
            res += 1
            continue

        cnt = 0
        
        for i in range(1, int(n ** 0.5) + 1):                                           # 제곱근까지 탐색
            if not n % i:
                if n // i == i:
                   cnt += 1                                                             # 제곱수면 카운트 + 1
                else:
                    cnt += 2                                                            # 일반 약수면 짝이 있으므로 카운트 + 2

            if cnt > limit:                                                             # limit 초과하면 바로 종료
                res += power
                break
        else:
            res += cnt

    return res

# 다른 사람의 풀이
def cf(n):                                                                              # 공약수 출력
    a = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a.append(n // i)
            a.append(i)
    return len(set(a))

def solution(number, limit, power):
    return sum([cf(i) if cf(i) <= limit else power for i in range(1, number + 1)])      # 풀어서 cf(i) 한 번만 쓰는게 좋다고 함

'''
회고 / TIL
- 무턱대고 풀었다가 시간 초과 발생해서, 제곱근까지 탐색했으나 이것도 시간 초과 발생함.
- 제곱근이 아닌 약수는 짝이 존재하므로 카운트를 2번 해서 빠르게 세고, limit에 도달하자마자 종료하게 해야 겨우 성공하는 것 같음.
- 다른 사람의 풀이는 볼 때마다 신기하긴 한데, 그렇게 하고 싶진 않음.
'''