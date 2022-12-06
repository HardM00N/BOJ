# https://www.acmicpc.net/problem/1021

# 나의 풀이 (Python3 72ms)
N, _ = map(int, input().split())
queue = [i + 1 for i in range(N)]
tests = list(map(int, input().split()))

cnt = 0

for test in tests:

    idx = queue.index(test)                     # 현재 큐에서 뽑으려는 수의 인덱스
    
    if idx > len(queue) // 2:                   # 찾으려는 수가 오른쪽에 있으면
        cnt += len(queue) - idx                 # 오른쪽으로 밀어야하는 만큼 카운트
    
    else:                                       # 찾으려는 수가 왼쪽에 있으면 
        cnt += idx                              # 왼쪽으로 밀어야하는 만큼 카운트

    queue = queue[idx:] + queue[:idx]           # 실제로 인덱스만큼 오른쪽 / 왼쪽으로 밀기
    queue.pop(0)                                # 밀고 나서 뽑으려는 수가 맨 앞에 왔으므로 제거

print(cnt)


'''
회고 / TIL
- 요세푸스 문제와 비슷한 문제임. 인덱스를 잘 관리해야함. 
- 다른 사람의 풀이도 대체로 비슷한 거 같아서, 생략함.
'''