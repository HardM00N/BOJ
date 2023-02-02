# https://school.programmers.co.kr/learn/courses/30/lessons/138477

#  나의 풀이
import heapq

def solution(k, score):
    res = []
    queue = []

    for i in score:                         
        heapq.heappush(queue, i)
        
        if len(queue) > k:                  # 힙이 k보다 커지면
            heapq.heappop(queue)            # 최솟값 제거

        res.append(queue[0])                # 현재 힙에서의 최솟값 append

    return res

# 다른 사람의 풀이
def solution(k, score):
    q = []
    answer = []
    
    for s in score:
        q.append(s)
        
        if (len(q) > k):
            q.remove(min(q))                # min을 이용한 풀이
        
        answer.append(min(q))

    return answer

'''
회고 / TIL
- 고민을 좀 하다가 최근에 CLASS 3++에서 익힌 heapq를 활용해서 풀었음.
- remove나 min을 활용한 풀이보다는 효율적이지 싶음.
'''