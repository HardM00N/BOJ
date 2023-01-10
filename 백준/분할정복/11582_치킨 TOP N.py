# https://www.acmicpc.net/problem/11582

# 나의 풀이 (Python3 1912ms)
N = int(input())
scores = list(map(int, input().split()))
K = int(input())

def merge_sort(N, scores, K):                                                       # merge sort

    if N == 2:
        return sorted(scores)
    
    else:
        N //= 2
        temp = merge_sort(N, scores[:N], K) + merge_sort(N, scores[N:], K)          # 2분할 재귀 호출
        
        if N == K:                                                                  # N이 K와 같아지면 이 단계까지의 정렬 결과 출력
            print(*temp)
        
        return sorted(temp)

merge_sort(N, scores, N // K)

# 다른 사람의 풀이 (Python3 856ms)
import sys

n = int(sys.stdin.readline())
table = list(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline())

answer = []

std = n // k
for con in range(k):
    answer.extend(sorted(table[con * std:(con+1) * std]))                           # 반복적으로 부분 정렬해 결과에 추가

print(" ".join(map(str, answer)))

'''
회고 / TIL
- 문제 읽고 보니 합병 정렬인데, 특정 단계까지의 결과를 출력하는 부분이 추가된 문제임.
- 병합 정렬은 분할 정복을 활용한 대표적인 예임.
- 본 문제는 재귀적으로 분할하지 않고, 반복문으로 부분적으로 정렬해서 풀 수도 있었음.
'''