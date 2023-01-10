# https://www.acmicpc.net/problem/2343

# 나의 풀이 (Python 3 616ms)
N, M = map(int, input().split())
clips = list(map(int, input().split()))

start = max(clips)                                  # 가장 큰 동영상 길이부터
end = sum(clips)                                    # 모든 동영상 길이의 합까지 탐색

while start <= end:
    mid = (start + end) // 2
    cnt, sum = 0, 0
    
    for i in range(N):
        if sum + clips[i] > mid:                    # 동영상을 합해서 mid보다 크면
            cnt += 1                                # 블루레이 개수 카운트
            sum = 0                                 # 합은 초기화
        sum += clips[i]

    if sum:                                         # 나머지가 남으면
        cnt += 1                                    # 블루레이 개수 + 1

    if cnt > M:                                     # 블루레이 개수가 M보다 많으면
        start = mid + 1                             # 더 큰 용량의 블루레이 필요
    else:                                           # 블루레이 개수가 M보다 작거나 같으면
        end = mid - 1                               # 블루레이의 용량을 최소화

print(end + 1)

'''
회고 / TIL
- 쉽게 생각했던 이진 탐색이 여기선 많이 어려웠음.
- 처음에 계수 정렬처럼 디스크들의 합을 배열로 표현하다가, 코드가 많이 길어지면서 생각이 꼬였음.
- 차근차근 간단한 방법을 찾는 연습을 하자.
'''