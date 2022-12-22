# https://school.programmers.co.kr/learn/courses/30/lessons/12982

# 나의 풀이
def solution(d, budget):
    cnt = 0
    
    for i in sorted(d):         # 오름차순으로 정렬
        budget -= i             
        
        if budget < 0:          # 예산 초과 시 종료
            break
        
        cnt += 1                # 그렇지 않다면 부서 카운트

    return cnt

# 다른 사람의 풀이
def solution(d, budget):
    d.sort()
    
    while budget < sum(d):      # 합계가 예산 범위에 들어올 때까지 pop
        
        d.pop()
    
    return len(d)

'''
회고 / TIL
- 최대한 많은 부서를 정해진 예산에서 해결 -> 금액이 적은 부서부터 해결하면 됨.
- 다른 사람의 풀이를 봤는데 그다지 효율적인 거 같진 않음.
'''