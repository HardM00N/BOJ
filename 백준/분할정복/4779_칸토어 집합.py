# https://www.acmicpc.net/problem/4779

# 나의 풀이 (Python3 48ms)
def cantor_set(N, line):
        if N == 1:
            return line
        else:
            N //= 3
            return cantor_set(N, line[:N]) + ' ' * N + cantor_set(N, line[N * 2:N * 3])     # 3분할 칸토어 재귀 호출

while 1:
    try:
        N = int(input())
        line = '-' * 3 ** N

        if N:
            print(cantor_set(3 ** N, line))
        else:                                                                               # N이 0이면 바로 출력
            print(line)
        
    except EOFError:                                                                        # 입력이 끝나면 종료
        break

# 다른 사람의 풀이 (Python3 36ms)
result = ['' for _ in range(13)]
result[0] = '-'

for i in range(1, 13):                                                                      # 반복하면서 먼저 계산한 부분을 이용해 채워나감
    result[i] = result[i-1] + ' '*3**(i-1) + result[i-1]

while True:
    try:
        print(result[int(input())])
    except:
        break

'''
회고 / TIL
- 분할 정복 재밌음.
- 풀이 4등했음.
- 나는 재귀적으로 푸는 습관이 있는데, 반복적으로 푼 풀이가 1등이었음.
'''