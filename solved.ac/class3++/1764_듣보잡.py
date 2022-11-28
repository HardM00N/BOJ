# https://www.acmicpc.net/problem/1764

# 나의 풀이 (Python3 108ms)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
names = set()
results = set()

for _ in range(N):                              # 중복 없으므로 set 자료형 활용
    names.add(input())

for _ in range(M):
    name = input()
    if name in names:                           # 앞 세트에 있으면 뒷 세트에 추가
        results.add(name)

print(len(results))
for result in sorted(results):                  # 뒷 세트 정렬 후 출력
    print(result.rstrip())

# 다른 사람의 풀이 (Python3 96ms)
import sys
n, m = map(int, input().split())
nameList = sys.stdin.read().splitlines()        # 하나의 리스트로 받음

hearset = set(nameList[:n])
seeset = set(nameList[n:])

ret = list(hearset & seeset)                    # 교집합 연산
ret.sort()

print(len(ret))
for i in ret:
    print(i)

'''
회고 / TIL
- 중복되는 데이터가 없다는 조건을 보고 set 자료형을 활용해서 품. 
- 다른 사람의 풀이를 보니 교집합으로 푼 걸 보고 신기했음. 
'''