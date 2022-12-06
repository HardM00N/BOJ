# https://www.acmicpc.net/problem/1158

# 나의 풀이 (Python3 84ms)
N, K = map(int, input().split())
data = [i + 1 for i in range(N)]
results, idx = [], K - 1                    # 초기 인덱스는 K번째이므로 K - 1

while data:
    if idx >= len(data):                    # 인덱스가 리스트의 길이보다 크면
        idx -= len(data)
    else:
        results.append(data.pop(idx))
        idx += K - 1                        # 다음 인덱스는 K만큼 증가하고, 데이터 하나가 pop()되었기 때문에 1을 빼줌

print('<' + str(results)[1:-1] + '>')

'''
회고 / TIL
- 다른 풀이들도 거의 비슷해서 생략함. 
- 인덱스 관리가 중요함.
'''