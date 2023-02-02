# https://school.programmers.co.kr/learn/courses/30/lessons/131128

# 첫 번째 풀이 (시간 초과)
from collections import Counter

def solution(X, Y):
    x, y = Counter(X), Counter(Y)
    ans = ''

    for k in x:
        if k in y:
            ans += k * min(x[k], y[k])
    
    if ans:
        if int(ans):
            return ''.join(sorted(ans, reverse=True))
        else:
            return '0'
    else:
        return '-1'

# 두 번째 풀이 (시간 초과)
def solution(X, Y):
    ans = ''

    x, y = Counter(X), Counter(Y)
    inter = set(X) & set(Y)

    for i in sorted(inter, reverse=True):
        ans += i * min(x[i], y[i])
    
    if ans:
        if int(ans):                                            # int()에서 시간 초과 발생
            return ans
        else:
            return '0'
    else:
        return '-1'

# 세 번째 풀이 (시간 초과)
def solution(X, Y):
    ans = ''

    a = {str(i):0 for i in range(9, -1, -1)}
    b = {str(i):0 for i in range(9, -1, -1)}

    for x in X:
        a[x] += 1
    for y in Y:
        b[y] += 1

    for k in a:
        if a[k] != 0 and b[k] != 0:
            ans += k * min(a[k], b[k])
    
    if ans:
        if int(ans):
            return ans
        else:
            return '0'
    else:
        return '-1'

# 네 번째 풀이
def solution(X, Y):
    ans = ''

    x, y = Counter(X), Counter(Y)
    inter = set(X) & set(Y)

    for i in sorted(inter, reverse=True):
        ans += i * min(x[i], y[i])
    
    if ans:
        if sum(list(map(int, list(ans)))):                      # 리스트의 합으로 대체
            return ans
        else:
            return '0'
    else:
        return '-1'

'''
회고 / TIL
- TC 11 ~ 15에서 시간 초과가 발생해서 1시간 넘게 삽질했음.
- 처음엔 반복문이나 Counter가 문제인가 싶어서 set로도, 계수 정렬로도, 여러 방식으로 풀어도 여전히 시간이 초과됨.
- 이것저것 해보다가 결국 찾아낸 문제가 0을 판별할 때 int를 사용한 것이었음.
- 해당 부분을 리스트의 합으로 계산하도록 수정하니 내가 만든 모든 풀이가 통과됨...
'''