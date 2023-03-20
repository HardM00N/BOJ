# https://school.programmers.co.kr/learn/courses/30/lessons/42587

# 나의 풀이
import heapq

def solution(priorities, location):
    queue = []
    cnt = 1                                     # 출력 순서 초기화

    for p in priorities:
        heapq.heappush(queue, -p)               # 최대 힙으로 쓰려면 -붙여서 push
    
    while queue:
        for i in range(len(priorities)):
            if priorities[i] == -queue[0]:
                if i == location:               # location에 해당하는 문서가 출력될 예정이라면
                    return cnt                  # cnt 리턴
                heapq.heappop(queue)            # 아니라면 앞 문서들을 출력하면서
                cnt += 1                        # 하나씩 카운트

'''
회고 / TIL
- 우선순위 큐 -> 힙을 떠올려서 풀었음.
- 복습 차 적어두자면 파이썬의 heapq는 최소 힙만 지원해서 최대 힙으로 쓰려면 push, pop 때 -를 붙이면 됨.
'''