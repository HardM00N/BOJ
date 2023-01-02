# https://www.acmicpc.net/problem/18870

# 첫 번째 풀이 (시간 초과)
_ = input()
coords = list(map(int, input().split()))

new_coords = sorted(set(coords))

for coord in coords:
    print(new_coords.index(coord), end=' ')             # index()에서 시간 초과 발생

# 두 번째 풀이 (Python3 1944ms)
_ = input()
coords = list(map(int, input().split()))
new_coords = sorted(set(coords))                        # 중복 제거하면서 정렬
new_dic = {}

for i in range(len(new_coords)):
    new_dic[new_coords[i]] = i

for coord in coords:
    print(new_dic[coord], end=' ')                      # 딕셔너리로 기록해두고 바로 찾기

'''
회고 / TIL
- 실버2에서 모처럼 쉬운 문제...인 줄 알았으나 어림없이 시간 초과
- index()에서 이미 구했던 숫자의 인덱스더라도 매번 다시 O(N)만큼 불필요하게 계산하기 때문에 시간 초과가 된 것으로 보임.
- 딕셔너리에 해당 숫자의 인덱스를 미리 기록해두고, 출력하는 방식으로 바꾸니 해결됨.
- 다른 사람의 풀이도 거의 비슷함.
'''