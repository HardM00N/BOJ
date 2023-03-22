# https://www.acmicpc.net/problem/23253

# 나의 풀이 (Python3 252ms)
import sys
input = sys.stdin.readline

_, M = map(int, input().split())

for _ in range(M):
    input()
    dummy = list(map(int, input().split()))
    
    if sorted(dummy, reverse=True) != dummy:        # 항상 스택은 내림차순이어야만 정리가 가능
        print('No')                                 # 내림차순이 아니었을 경우 정리 불가하므로 break
        break

else:                                               # 모든 스택이 내림차순이었다면
    print('Yes')                                    # 정리 가능

# 다른 사람의 풀이 (Python3 152ms)
import sys
input = sys.stdin.readline

def sol():
    N, M = map(int,input().split())
    for _ in range(M):
        input()
        min = N + 1                                 # 미리 비교할 min을 선언하고
        for num in map(int, input().split()):
            if num > min:                           # 들어온 값이 min보다 작은지 확인하면서
                return "No"
            min = num                               # min 최신화
    return "Yes"    

print(sol())

'''
회고 / TIL
- 문제의 핵심은 들어오는 책 더미들이 내림차순인지 확인하는 것임. 
- 나는 내림차순으로 정렬한 더미와 실제 더미를 비교해서 풀었기 때문에, 정렬에서 시간이 소요됨.
- 다른 사람의 풀이는 정렬보다 더미의 번호를 하나씩 확인하면서 전의 번호보다 작은지 체크했기 때문에 효율적임.
'''