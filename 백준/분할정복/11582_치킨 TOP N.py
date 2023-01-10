# https://www.acmicpc.net/problem/11582

N = int(input())
scores = list(map(int, input().split()))
K = int(input())

def merge_sort(N, scores, K):
    if N == 1:
        return scores
    else:
        N //= 2