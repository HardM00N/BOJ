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
    if i == 1:
        continue
    for j in range(1, int(i ** 0.5) + 1):   # 1부터 제곱근까지만 순회
        if i % j == 0:
            cnt += 1
        if cnt == 2:    # 1 말고도 약수가 있으면 종료
            break
    if cnt == 1:    # 약수가 1 뿐이면 출력
        print(i)

'''
회고 / TIL
- 저번 1978번 문제처럼 풀었다가 가볍게 시간 초과됨. 
- 소수 판별법을 검색해보니 제곱근까지만 약수를 탐색해도 된다는 사실을 알게 되었음. 
- 에라토스테네스의 체 (오랜만에 들어봄) 방법으로 풀 수도 있는 것 같음. 
'''