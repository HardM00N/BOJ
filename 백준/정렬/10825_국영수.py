# https://www.acmicpc.net/problem/10825

# 나의 풀이 (Python3 428ms)
import sys
input = sys.stdin.readline

db = []

for _ in range(int(input())):                               # 리스트에 추가
    name, kor, eng, math = input().split()
    db.append([name, int(kor), int(eng), int(math)])

db.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))           # 각 기준을 순서대로 정렬

for i in db:
    print(i[0])

# 다른 사람의 풀이 (Python3 280ms)
import sys
input = sys.stdin.readline

def parse_line(line):
    name, kor, eng, math = line.split(' ')
    kor, eng, math = int(kor), int(eng), int(math)
    return -kor, eng, -math, name                           # 애초에 내림차순은 음수로 받고, 정렬 순서대로 리턴함

N = int(input())
data = [parse_line(input()) for _ in range(N)]
print(*map(lambda x:x[3], sorted(data)), sep='\n')          # 한 번에 정렬

'''
회고 / TIL
- 단순히 문제에 입각해 정렬하면 되는 문제지만, 시간 복잡도는 천차만별인 것 같음.
- 애초에 내림차순은 음수로 받고, 정렬할 규칙 순서대로 항목을 받아서 sorted() 한 번으로 정렬한 풀이가 가장 빨라보였음.
'''