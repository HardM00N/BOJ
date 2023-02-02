# https://www.acmicpc.net/problem/11656

# 나의 풀이 (Python3 48ms)
S = input()
S_list = []

for i in range(len(S)):
    S_list.append(S[i:])                        # 접미사 리스트 만들기

for s in sorted(S_list):                        # 정렬해서 출력
    print(s)

# 다른 사람의 풀이
s = input()
print(*sorted(s[i:] for i in range(len(s))))    # 컴프리헨션

'''
회고 / TIL
- 단순한 정렬 문제임.
'''