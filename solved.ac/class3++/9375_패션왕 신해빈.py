# https://www.acmicpc.net/problem/9375

# 나의 풀이 (Python3 68ms)
import sys
input = sys.stdin.readline

for _ in range(int(input())):                       # 테스트 케이스
    cloths = {}
    result = 1                                      # 조합을 곱할 result 초기화

    for _ in range(int(input())):
        c_name, c_class = input().split()
        if c_class in cloths:                       # 이미 key가 딕셔너리에 있으면
            cloths[c_class].append(c_name)          # 해당 key에 value 추가
        else:                                       # 아직 key가 딕셔너리에 없다면
            cloths[c_class] = [c_name]              # 해당 key에 value 생성
        
    for value in cloths.values():
        result *= (len(value) + 1)                  # 각 key마다 value + 1를 곱하고
    
    print(result - 1)                               # 결과에서 1을 뺌 (모두 안 입는 경우)

'''
회고 /  TIL
- 옷의 종류별로 단순히 조합해주면 풀 수 있는 문제임. 
- defaultdict가 아닌 일반 딕셔너리에도 하나의 key에 여러 개의 value를 추가할 수 있어서, 이를 이용함.
- 다른 사람의 풀이도 비슷한 방식이라, 리뷰는 생략함.
'''