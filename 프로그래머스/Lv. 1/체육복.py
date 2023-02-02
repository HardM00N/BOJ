# https://school.programmers.co.kr/learn/courses/30/lessons/42862

# 첫 번째 풀이 (5, 12번 테스트케이스 실패) -> 여벌이 있으면서 도난당한 친구들 때문...
def solution(n, lost, reserve):

    lost = set(lost)
    reserve = set(reserve)

    cnt = n - len(lost)

    for i in lost:
        if i in reserve:
            cnt += 1
            reserve.remove(i)
        elif i - 1 in reserve:
            cnt += 1
            reserve.remove(i - 1)
        elif i + 1 in reserve:
            cnt += 1
            reserve.remove(i + 1)
        
    return cnt

# 두 번째 풀이
def solution(n, lost, reserve):

    lost = set(lost)
    reserve = set(reserve)

    inter = lost & reserve                          # 여벌이 있지만 도난당한 친구들 제외
    lost -= inter
    reserve -= inter

    cnt = n - len(lost)                             # 도난당하지 않은 친구들 카운트
    
    for i in lost:                                  # 도난 당했는데
        if i - 1 in reserve:                        # 앞 번호나
            cnt += 1
            reserve.remove(i - 1)
        elif i + 1 in reserve:                      # 뒷 번호가 여벌이 있었다면 카운트
            cnt += 1
            reserve.remove(i + 1)
        
    return cnt

'''
회고 / TIL
- 대뜸 풀었건만 여벌이 있으면서 도난당한 친구들 때문에 5, 12 테스트케이스를 통과하지 못함.
- 도난당했지만 여벌이 있는 사람이면 제외하도록 if문에서 제외를 시켜줬다고 생각했지만, 앞이나 뒷 번호의 여벌 없이 도난당한 사람이 먼저 가져가버릴 수가 있었음.
- 교집합을 미리 제거해주니 무사히 통과함.
'''