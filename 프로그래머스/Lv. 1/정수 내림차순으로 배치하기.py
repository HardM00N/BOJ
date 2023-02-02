# https://school.programmers.co.kr/learn/courses/30/lessons/12933

# 나의 풀이
def solution(n):
    return int(''.join(s for s in sorted(str(n), reverse=True)))

'''
회고 / TIL
- 다른 사람의 풀이보다 내 풀이가 더 간단한 것 같아서 생략함. 
- join()을 활용해 sorted의 결과로 리스트가 된 문자열을 다시 str형으로 바꿀 수 있었음. 
'''