# https://www.acmicpc.net/problem/1780

# 첫 번째 풀이 (Python3 시간 초과)
import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

cnt1, cnt2, cnt3 = 0, 0, 0                                                                                                              # 실제 -1, 0, 1 종이의 카운트 변수

def cnt_paper(paper, n):
    global cnt1
    global cnt2
    global cnt3
    
    c1, c2, c3 = 0, 0, 0                                                                                                                # 인자로 들어온 paper의 카운트만을 위한 임시 변수
    
    for p in paper:                                                                                                                     # 전체에 대해 -1, 0, 1 카운트
        c1 += p.count(-1)
        c2 += p.count(0)
        c3 += p.count(1)
 
    if c1 == n ** 2 or c2 == n ** 2 or c3 == n ** 2:                                                                                    # -1, 0, 1의 한 가지 수로만 이루어져 있다면
        if c1 == n ** 2:
            cnt1 += 1
        elif c2 == n ** 2:
            cnt2 += 1
        else:
            cnt3 += 1            
        return

    else:                                                                                                                               # 한 가지 수로만 이루어져 있지 않다면 분할 정복
        for row in range(3):
            for col in range(3):
                cnt_paper([p[(n // 3) * col:(n // 3) * (col + 1)] for p in paper[(n // 3) * row:(n // 3) * (row + 1)]], n // 3)
    
cnt_paper(paper, N)
print(cnt1, cnt2, cnt3, sep='\n')

# 두 번째 풀이 (Python3 7408ms)
import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

cnt1, cnt2, cnt3 = 0, 0, 0                                                                                                              # 실제 -1, 0, 1 종이의 카운트 변수

def cnt_paper(paper, n):
    global cnt1
    global cnt2
    global cnt3
    
    c1, c2, c3 = 0, 0, 0                                                                                                                # 인자로 들어온 paper의 카운트만을 위한 임시 변수
    
    for p in paper:                                                                                                                     # 전체에 대해 -1, 0, 1 카운트
        c1 += p.count(-1)
        c2 += p.count(0)
        c3 += p.count(1)
 
    if c1 == n ** 2 or c2 == n ** 2 or c3 == n ** 2:                                                                                    # -1, 0, 1의 한 가지 수로만 이루어져 있다면
        if c1 == n ** 2:
            cnt1 += 1
        elif c2 == n ** 2:
            cnt2 += 1
        else:
            cnt3 += 1            
        return

    else:
        n //= 3
                                                                                                                                       # 한 가지 수로만 이루어져 있지 않다면 분할 정복
        p1 = [p[:n] for p in paper[:n]]
        cnt_paper(p1, n)
        p2 = [p[n:n + n] for p in paper[:n]]
        cnt_paper(p2, n)
        p3 = [p[n + n:] for p in paper[:n]]
        cnt_paper(p3, n)
        
        p4 = [p[:n] for p in paper[n:n + n]]
        cnt_paper(p4, n)
        p5 = [p[n:n + n] for p in paper[n:n + n]]
        cnt_paper(p5, n)
        p6 = [p[n + n:] for p in paper[n:n + n]]
        cnt_paper(p6, n)
        
        p7 = [p[:n] for p in paper[n + n:]]
        cnt_paper(p7, n)
        p8 = [p[n:n + n] for p in paper[n + n:]]
        cnt_paper(p8, n)
        p9 = [p[n + n:] for p in paper[n + n:]]
        cnt_paper(p9, n)
    
cnt_paper(paper, N)
print(cnt1, cnt2, cnt3, sep='\n')

'''
회고 / TIL
- 구현도 쉽지 않았지만 시간 초과가... 엄청 발생함...
- 첫 번째 풀이에서의 2중 반복문을 그냥 9개의 함수 호출로 펼쳐서 수정하니 통과했음.
- 다른 사람의 풀이를 보니 DFS로 푸는게 빠르더라...
'''