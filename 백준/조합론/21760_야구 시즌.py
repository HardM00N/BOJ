# https://www.acmicpc.net/problem/21760

'''
* nCr = n-COMB-r로 표기

같은 지역 리그 : M-COMB-2 * N * A
다른 지역 리그 : N-COMB-2 * M * M * B
'''

# 나의 풀이 (Python3 44ms)
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, M, k, D = map(int, input().split())
    total = (M * (M - 1) // 2 * N * k) + (N * (N - 1) // 2 * M * M)     # 내부 리그 + 외부 리그

    if total <= D:
        print(D - (D % total))
    else:
        print(-1)

'''
회고 / TIL
- 실버 5치곤 시간 꽤 걸렸음.
- 처음엔 while 문으로 D에 근접한 최댓값을 브루트포스로 찾아서 부분만 통과함. 
- 아예 D에서 total을 나눠서 최대 경기 수가 나오게끔 수정하니 풀림. 사람들 풀이 형태만 다르지 거의 비슷함.
'''