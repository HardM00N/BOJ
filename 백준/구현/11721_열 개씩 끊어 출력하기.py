# https://www.acmicpc.net/problem/11721

# 나의 풀이 (Python3 36ms)
s = input()
nines = set([9, 19, 29, 39, 49, 59, 69, 79, 89])            # 10마다 끊어주기 위한 set

for i, j in enumerate(s):                                   # 문자열을 돌면서
    print(j, end='')                                        # 출력하다가

    if i in nines:                                          # 10마다 개행 출력
        print()

# 다른 사람의 풀이 (Python3 32ms)
def solution():
    line = input()
    i = 0
    
    while i < len(line):
        print(line[i:i+10])                                 # 슬라이싱으로 출력
        i += 10

if __name__=="__main__":
    solution()

'''
회고 / TIL
- 쉬운 문제지만 여러 풀이 방법이 존재함.
- 다양한 풀이법을 눈에 익혀놓는 것이 좋을 것 같음.
'''