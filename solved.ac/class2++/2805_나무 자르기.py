'''
상근이는 나무 M미터가 필요하다. 
근처에 나무를 구입할 곳이 모두 망해버렸기 때문에, 정부에 벌목 허가를 요청했다. 
정부는 상근이네 집 근처의 나무 한 줄에 대한 벌목 허가를 내주었고, 상근이는 새로 구입한 목재절단기를 이용해서 나무를 구할 것이다. 

목재절단기는 다음과 같이 동작한다. 
먼저, 상근이는 절단기에 높이 H를 지정해야 한다. 높이를 지정하면 톱날이 땅으로부터 H미터 위로 올라간다. 
그 다음, 한 줄에 연속해있는 나무를 모두 절단해버린다. 따라서, 높이가 H보다 큰 나무는 H 위의 부분이 잘릴 것이고, 낮은 나무는 잘리지 않을 것이다. 

예를 들어, 한 줄에 연속해있는 나무의 높이가 20, 15, 10, 17이라고 하자. 
상근이가 높이를 15로 지정했다면, 나무를 자른 뒤의 높이는 15, 15, 10, 15가 될 것이고,
상근이는 길이가 5인 나무와 2인 나무를 들고 집에 갈 것이다. (총 7미터를 집에 들고 간다)
절단기에 설정할 수 있는 높이는 양의 정수 또는 0이다. 

상근이는 환경에 매우 관심이 많기 때문에, 나무를 필요한 만큼만 집으로 가져가려고 한다. 
이 때, 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.
'''

# 첫 번째 풀이
import sys
input = sys.stdin.readline

_, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 1
end = max(trees)                        # 이진 탐색은 가장 높은 나무까지 수행

while start <= end:
    mid = (start + end) // 2
    total = 0                           # 나무를 잘라 얻은 합을 저장할 변수
    
    for tree in trees:
        if tree >= mid:                 # 나무를 잘랐을 때 결과가 0 이상일 때만 total에 저장
            total += tree - mid         # 음수가 저장되면 올바른 연산이 안 되기 때문

    if total < M:
        end = mid - 1
    else:
        start = mid + 1

print(end)



# 두 번째 풀이
import sys
input = sys.stdin.readline
from collections import Counter

_, M = map(int, input().split())
trees = Counter(map(int, input().split()))

start = 1
end = max(trees)

while start <= end:
    mid = (start + end) // 2
    total = 0                               # 나무를 잘라 얻은 합을 저장할 변수
    
    for tree, i in trees.items():
        if tree >= mid:                     # 나무를 잘랐을 때 결과가 0 이상일 때만 total에 저장
            total += (tree - mid) * i       # 음수가 저장되면 올바른 연산이 안 되기 때문

    if total < M:
        end = mid - 1
    else:
        start = mid + 1

print(end)



# 추가 풀이 (첫 번째 풀이에 리스트 컴프리헨션 적용)
import sys
input = sys.stdin.readline

_, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 1
end = max(trees)                        # 이진 탐색은 가장 높은 나무까지 수행

while start <= end:
    mid = (start + end) // 2
    total = sum(tree - mid for tree in trees if tree > mid)

    if total < M:
        end = mid - 1
    else:
        start = mid + 1

print(end)

'''
회고 / TIL
- 이진 탐색으로 풀었음에도 시간초과의 벽에 부딪혀서 한참을 고민했음. 
- 불필요한 변수를 줄이니(result 필요없이 바로 end 출력) 아슬아슬하게 통과됨. (첫 번째 풀이, 4812ms)
- 다른 사람의 풀이를 보니 Counter를 활용해 for문 내에서 획기적으로 시간을 줄였음. 
- 이를 토대로, 두 번째 풀이를 작성해서 안전하게 통과함. (472ms)
- 시간 제한이 1초인데, 첫 번째 풀이에서 4812ms가 어떻게 통과됐는지는 잘 모르겠음. 
- 위의 두 개의 풀이에도 개선할 점이 여전히 있음. 리스트 컴프리헨션을 사용하면 시간을 더 단축할 수 있는데, 아직 익숙치가 않음.
- 넘을 산이 많다...
'''