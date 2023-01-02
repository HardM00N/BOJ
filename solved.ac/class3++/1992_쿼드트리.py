# https://www.acmicpc.net/problem/1992

# 나의 풀이 (Python3  48ms)
import sys
input = sys.stdin.readline

N = int(input())
signal = [input().strip() for _ in range(N)]

def quad_tree(signal, N):
    c0, c1 = 0, 0                                                                                           # 완전히 압축되었는지 확인하는 변수

    for s in signal:                                                                                        # 모든 영상을 돌며 0 혹은 1 카운트
        c0 += s.count('0')
        c1 += s.count('1')

    if c0 == N ** 2 or c1 == N ** 2:                                                                        # 모든 영상이 0 혹은 1로만 이루어져있으면
        if c0 == N ** 2:
            print(0, end='')                                                                                # 해당 숫자 출력 후 종료
        else:
            print(1, end='')
        return

    else:                                                                                                   # 영상에 0과 1이 섞여있다면
        print('(', end='')                                                                                  # 괄호 열기

        N //= 2                                                                                             # 4분할 정복
        for row in range(2):
            for col in range(2):
                quad_tree([s[N * col:N * (col + 1)] for s in signal[N * row:N * (row + 1)]], N)
        
        print(')', end='')                                                                                  # 재귀호출이 끝나면 괄호 닫기

quad_tree(signal, N)


# 다른 사람의 풀이 (Python3 36ms)
import sys

n = int(sys.stdin.readline().rstrip())
data = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

def checkAllSame(n, x, y):
  result = ""
  base = data[x][y]
  for i in range(x, x + n):                                                                                 # 모든 data를 순회하면서
    for j in range(y, y + n):
      if not data[i][j] == base:                                                                            # 처음 base와 다른 값을 발견하면
        result += checkAllSame(n // 2, x, y)                                                                # 4분할 정복
        result += checkAllSame(n // 2, x, y + n // 2)
        result += checkAllSame(n // 2, x + n // 2, y)
        result += checkAllSame(n // 2, x + n // 2, y + n // 2)
        return "(" + result + ")"                                                                           # 분할 정복 결과의 앞 뒤에 괄호 추가
  return data[x][y]

print(checkAllSame(n, 0, 0))

'''
회고 / TIL
- 앞서 풀었던 색종이 만들기와 Z와 같은 4분할 정복 문제임.
- 0이나 1로만 이루어진 완전한 영상이 아닐 경우 앞 뒤로 괄호를 추가해주는 부분이 까다로웠음.
- 다른 사람의 풀이를 보니 나처럼 모든 영상에서의 0과 1을 카운트하기보다 첫 값과 다른 값을 발견하면 바로 재귀 호출하도록 짜서 시간을 줄인 것 같음. 참고하자.
- result의 앞 뒤로 괄호를 단순히 더해준 것도 인상적이었음.
- 분할 정복 재밌음.
'''