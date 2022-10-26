'''
집에서 시간을 보내던 오영식은 박성원의 부름을 받고 급히 달려왔다. 박성원이 캠프 때 N개의 랜선을 만들어야 하는데 너무 바빠서 영식이에게 도움을 청했다. 

이미 오영식은 자체적으로 K개의 랜선을 가지고 있다.
그러나 K개의 랜선은 길이가 제각각이다.

박성원은 랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에 K개의 랜선을 잘라서 만들어야 한다. 
예를 들어 300cm짜리 랜선에서 140cm짜리 랜선을 두 개 잘라내면 20cm는 버려야 한다. (이미 자른 랜선은 붙일 수 없다)

편의를 위해 랜선을 자르거나 만들 때 손실되는 길이는 없다고 가정하며, 
기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정하자. 
그리고 자를 때는 항상 센티미터 단위로 정수길이만큼 자른다고 가정하자. N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다. 
이 때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하시오. 
'''
# # 첫 번째 풀이 (시간 초과)
# import sys
# input = sys.stdin.readline

# utps = []

# K, N = map(int, input().split())
# for _ in range(K):
#     utps.append(int(input()))

# for length in range(sum(utps) // N, 0, -1):
#     cnt = 0
#     for utp in utps:
#         cnt += utp // length
#     if cnt == 11:
#         print(length)
#         break

# 두 번째 풀이 (이진 탐색, 답지 참고)
import sys
input = sys.stdin.readline

utps = []

K, N = map(int, input().split())
for _ in range(K):
    utps.append(int(input()))

# start, end = 1, max(utps)         # 답지에 있던 코드, 각 길이 중 최대 길이까지 불필요하게 탐색함. 
start, end = 1, sum(utps) // N      # 전체 길이의 합을 N으로 나눈 몫만큼만 탐색하면 됨. (시간 절약)

while start <= end:                 # 이진 탐색
    mid = (start + end) // 2
    cnt = 0
    for utp in utps:
        cnt += utp // mid

    if cnt >= N:                    # 분기점
        start = mid + 1
    else:
        end = mid - 1
print(end)                          # 최종 길이 출력

'''
회고 / TIL
- 문제 이해에 시간이 좀 걸렸지만, 구현에 성공했는데 제출하고보니 시간 초과가 났다. (역시 100만 이상이라서 불안했음)
- 결국 문제 유형을 확인해보니 이진 탐색으로 풀어야 했음. 기억이 가물가물해 답지를 참고함. 
- 답지를 보니 너무나 간단한 구현에 속상했지만, 이번 기회에 이진 탐색 코드는 확실히 외워야겠음. 답지에 불필요한 부분을 약간 수정함. 
'''