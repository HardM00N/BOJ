# https://www.acmicpc.net/problem/17626

# 첫 번째 풀이 -> 틀림 : 무조건 큰 걸 나눈다고 최소 개수가 아님!
n = int(input())
cnt = 0

for i in range(n // 2, 0, -1):
    if n - (i ** 2) >= 0:
        n -= (i ** 2)
        cnt += 1
        
        if i == 1:
            cnt += n

print(cnt)

# 두 번째 풀이 (Python3 시간 초과... PyPy3 160ms)
n = int(input())
sq = [x ** 2 for x in range(1, 224)]            # 50000 이하의 제곱수들
cnt = 4

for i in sq:                                    # 제곱수 세 가지로 합해지면
    for j in sq:
        for k in sq:
            if i + j + k == n:
                cnt = 3

for i in sq:                                    # 제곱수 두 가지로 합해지면
    for j in sq:
        if i + j == n:
            cnt = 2

for i in sq:                                    # 제곱수 하나로 나오면
    if i == n:
        cnt = 1

print(cnt)                                      # 만약 3, 2, 1도 아니면 초기값 4 출력

'''
회고 / TIL
- 코테 스터디 시작하고 역대급으로 어려웠던 문제...
- Python3 시간 초과의 벽을 뚫지 못하고 PyPy3만 겨우 통과함. 
- 다른 사람의 풀이를 보니 요것도 DP로 풀 수 있더라... 어떻게 그렇게 생각하지...
'''