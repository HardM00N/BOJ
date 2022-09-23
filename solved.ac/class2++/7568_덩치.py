'''
문제가 길어서 링크로 대체함. 
https://www.acmicpc.net/problem/7568
'''

N = int(input())
data = []

for _ in range(N):
    data.append(list(map(int, input().split())))
ranks = []
for i in range(N):
    rank = 1
    for j in range(N):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:

            rank += 1
    
    print(rank, end=' ')

'''
회고 / TIL
- 단순히 문제 조건대로 비교하면서 순위를 계산하면 풀림. 
- 오랜만에 보는... easy한 문제...
'''