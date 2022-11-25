# https://www.acmicpc.net/problem/1620

# 나의 풀이 (Python3 308ms / 61564KB)
import sys

input = sys.stdin.readline
N, M = map(int, input().split())

poke_dict1 = {}                             # 인덱스 : 포켓몬명 딕셔너리 (정방향)
poke_dict2 = {}                             # 포켓몬명 : 인덱스 딕셔너리 (역방향)

for idx in range(N):
    poke = input().rstrip()
    
    poke_dict1[str(idx + 1)] = poke         # 정방향 딕셔너리에 추가
    poke_dict2[poke] = str(idx + 1)         # 역방향 딕셔너리에 추가

for _ in range(M):
    keyword = input().rstrip()
    
    if keyword in poke_dict1:               # keyword가 정방향 딕셔너리의 key라면
        print(poke_dict1[keyword])          # 정방향 딕셔너리의 value인 포켓몬명 출력
    
    else:                                   # keyword가 역방향 딕셔너리의 key이므로
        print(poke_dict2[keyword])          # 역방향 딕셔너리의 value인 인덱스 출력

'''
회고 / TIL
- 처음엔 딕셔너리 하나로만 풀고, value로 key를 찾는 과정에서 for문을 이용했더니 시간초과에 부딪힘. 
- 그래서 딕셔너리를 애초에 정방향 / 역방향 두 개로 만들고, value로 key를 찾는 것도 빠르게 찾을 수 있도록 구현해서 해결함.
- 풀고 나서 다른 사람의 풀이를 보니 다양한 풀이법이 많은데, 딕셔너리를 사용하는 것은 공통된 점으로 보임. 
'''