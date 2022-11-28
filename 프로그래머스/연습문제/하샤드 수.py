# https://school.programmers.co.kr/learn/courses/30/lessons/12947?language=python3

# 나의 풀이
def solution(x):
    total = 0
    
    for num in str(x):                                  # str형으로 바꿔 각 자릿수의 합 계산
        total += int(num)   
    
    if x % total == 0:
        return True
    else:
        return False

# 다른 사람의 풀이
def Harshad(n):
    return n % sum([int(c) for c in str(n)]) == 0       # 리스트 컴프리헨션 활용


'''
회고 / TIL
- 확실히 기본 문제를 다시 푸니까, 알고리즘적인 부분보다는 리스트 컴프리헨션과 같은 다른 사람들의 스킬을 익힐 수 있어서 도움이 됨. 
- 나는 단순히 절차적으로 구현했지만, True / False를 리턴하는데 있어서 굳이 if문을 사용하지 않아도 해결이 되는 문제였음. 
'''