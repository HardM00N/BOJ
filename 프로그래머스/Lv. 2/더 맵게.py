# https://school.programmers.co.kr/learn/courses/30/lessons/42626

# 나의 풀이
import heapq

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)                                 # 힙으로 만들기
    
    while 1:
        min1 = heapq.heappop(scoville)

        if min1 >= K:                                       # 가장 작은 값이 K보다 크면 종료
            return cnt
        elif scoville:                                      # 아니라면 스코빌 섞기
            min2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min1 + min2 * 2)
            cnt += 1
        else:                                               # 섞을 스코빌이 없다면 불가능
            return -1

'''
회고 / TIL
- 최소 힙을 이용하면 쉬운 문제
'''