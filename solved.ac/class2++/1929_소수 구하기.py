'''
M 이상 N 이하의 소수를 모두 출력하는 프로그램을 작성하시오. 
'''

# 첫 번째 풀이 (시간 초과)
# M, N = map(int, input().split())

# for i in range(M, N + 1):
#     cnt = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             cnt += 1
#     if cnt == 2:
#         print(i)

# 두 번째 풀이
M, N = map(int, input().split())

for i in range(M, N + 1):
    cnt = 0
    for j in range(1, i + 1):
        if i % j == 0:
            cnt += 1
        if cnt > 2:
            break
    if cnt == 2:
        print(i)