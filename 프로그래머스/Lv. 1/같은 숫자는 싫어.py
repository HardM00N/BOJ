# https://school.programmers.co.kr/learn/courses/30/lessons/12906

# 나의 풀이
def solution(arr):
    ans = []
    idx = 0
    tmp = None
    
    while 1:
        try:
            if arr[idx] != tmp:                         # 현재 숫자와 tmp 비교
                ans.append(arr[idx])                    # 현재 숫자가 새로운 숫자라면 ans에 append하고
                tmp = arr[idx]                          # tmp에 현재 숫자 저장
            idx += 1
        except:                                         # index 에러가 발생하면 -> 리스트가 끝났으므로 종료
            break
        
    return(ans)

# 다른 사람의 풀이
def no_continuous(s):
    result = []
    
    for c in s:
        if (len(result) == 0) or (result[-1] != c):     # [-1]로 가장 최근 숫자와 비교
            result.append(c)
    
    return result

'''
회고 / TIL
- 처음에 정답 리스트에 append하는 방식이 아닌, 기존 arr에서 pop하는 방식으로 풀었더니 시간 초과됨.
- pop()은 O(1)이지만 pop(index)는 O(n)임. 주의하자.
- 다른 사람의 풀이들을 살펴보다가 슬라이싱은 인덱스 벗어나도 오류가 나지 않는다는 것을 처음 알게 되었음. 다음에 참고참고...
'''