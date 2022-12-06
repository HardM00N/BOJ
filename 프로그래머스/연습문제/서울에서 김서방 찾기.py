# https://school.programmers.co.kr/learn/courses/30/lessons/12919

# 나의 풀이
def solution(seoul):
    for idx, name in enumerate(seoul):
        if name == 'Kim':
           return '김서방은 {}에 있다'.format(idx)

# 다른 사람의 풀이
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))      # list.index 활용

'''
회고 / TIL
- 다른 사람의 풀이는 리스트의 index 메서드를 활용했지만, 어차피 시간복잡도는 O(n)으로 같음. 
'''