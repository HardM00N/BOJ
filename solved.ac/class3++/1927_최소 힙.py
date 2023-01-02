# https://www.acmicpc.net/problem/1927

'''
힙은 특정한 규칙을 갖는 트리로, 최댓값과 최솟값을 찾는 연산을 빠르게 하기 위해 고안된 완전이진트리를 기본으로 함.

힙 property : A가 B의 부모 노드이면, A의 키 값과 B의 키 값에는 대소 관계가 성립함.

- 최소 힙 : 부모 노드의 키 값이 자식 노드의 키 값보다 항상 작은 힙
- 최대 힙 : 부모 노드의 키 값이 자식 노드의 키 값보다 항상 큰 힙

이러한 속성으로 인해 힙에서는 가장 낮은(혹은 높은) 우선순위를 갖는 노드가 항상 루트에 오게 되고, 
이를 이용해 우선순위 큐와 같은 추상적 자료형을 구현할 수 있음.
이 때 키 값의 대소 관계는 부모-자식 간에만 성립하고, 형제 노드 상에는 대소 관계가 정해지지 않음.

파이썬 heapq 모듈은 heapq (priority queue) 알고리즘을 제공함.
모든 부모 노드는 자식 노드보다 값이 작거나 큰 이진트리 구조인데, 
내부적으로는 인덱스 0에서 시작해 K번째 원소가 항상 자식 원소들(2K+1, 2K+2)보다 작거나 같은 최소 힙의 형태로 정렬됨.

- heapq.heappush(heap, item) : item을 heap에 추가
- heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴함. 비어있는 경우 IndexError 발생
- heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 (in linear time, O(N))
'''

# 나의 풀이 (Python3 124ms)
import heapq
import sys
input = sys.stdin.readline

queue = []

for _ in range(int(input())):
    x = int(input())
    
    if x >= 1:                                  # x가 자연수라면
        heapq.heappush(queue, x)                # queue에 x 삽입
    elif x == 0:                                # x가 0이고
        if queue:                               # queue가 비어있지 않다면
            print(heapq.heappop(queue))         # 최솟값 제거하면서 출력
        else:
            print(0)

'''
회고 / TIL
- 이코테에서 heapq를 접했지만, 거의 까먹은 상태여서 개념을 다시 공부하고 풀었음.
- 트리 자료구조에 대해 완벽하게 숙지하지 못한 부분이 많아서, 다시 정리해야할 것 같다.
'''