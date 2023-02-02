import sys
input = sys.stdin.readline

db = []

for _ in range(int(input())):
    name, kor, eng, math = input().split()
    db.append([name, int(kor), int(eng), int(math)])

db.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in db:
    print(i[0])