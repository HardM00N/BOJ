# https://www.acmicpc.net/problem/18111


# 첫 번째 풀이 -> PyPy3만 통과, 788ms
# import sys
# input = sys.stdin.readline

# N, M, B = map(int, input().split())
# ground = []
# results = []

# for _ in range(N):
#     ground.append(list(map(int, input().split())))

# for height in range(min(map(min, ground)), max(map(max, ground)) + 1):
#     inven = B
#     time = 0

#     for i in range(N):
#         for j in range(M):
#             gap = ground[i][j] - height
#             if gap > 0:
#                 inven += gap
#                 time += 2 * gap
#             elif gap < 0:
#                 inven += gap
#                 time += 1 * -gap
    
#     if inven >= 0:
#         results.append((time, height))

# results.sort(key=lambda x: (x[0], -x[1]))
# print(results[0][0], results[0][1])

# 두 번째 풀이
import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
ground = []
results = []

for _ in range(N):
    ground.append(list(map(int, input().split())))

for height in range(min(map(min, ground)), max(map(max, ground)) + 1):
    inven = B
    time = 0

    for i in range(N):
        for j in range(M):
            gap = ground[i][j] - height
            if gap > 0:
                inven += gap
                time += 2 * gap
            elif gap < 0:
                inven += gap
                time += 1 * -gap
    
    if inven >= 0:
        results.append((time, height))

results.sort(key=lambda x: (x[0], -x[1]))
print(results[0][0], results[0][1])
