# https://www.acmicpc.net/problem/1032

# 나의 풀이 (Python3 36ms)
N = int(input())
files = []

for _ in range(N):
    files.append(input())

ans = list(files[0])                    # 정답의 기준은 첫 번째 파일명으로 설정

for i, ch in enumerate(files[0]):       # 파일명의 각 글자를 순회하면서
    for j in range(1, N):               # 여러 파일들의 해당 글자를 비교
        if ch != files[j][i]:           # 다른 글자가 있다면
            ans[i] = '?'                # 정답의 해당 글자를 ?로 대체
        
print(''.join(ans))

'''
회고 / TIL
- 기준을 정하고, 기준과 다른 파일들을 하나씩 비교하면서 다른 부분을 ?로 바꾸면 됨.
- 다른 사람의 풀이도 비슷함. 
'''