# https://school.programmers.co.kr/learn/courses/30/lessons/12954

# 나의 풀이
def solution(x, n):
    
    nums = []
    temp = 0

    for _ in range(n):
        
        nums.append(x + temp)
        temp += x
    
    return nums

# 다른 사람의 풀이
def number_generator(x, n):
    return [i * x + x for i in range(n)]    # 리스트 컴프리헨션 활용


'''
회고 / TIL
- 문제 그대로 구현해서 풀었지만, 리스트 컴프리헨션으로 한 줄이면 해결되는 문제였음. 
- 쓸데없는 변수를 사용하지 않도록 노력해야겠음. 
'''