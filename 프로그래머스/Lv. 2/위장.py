# https://school.programmers.co.kr/learn/courses/30/lessons/42578

# 나의 풀이
def solution(clothes):
    cnt = len(clothes)
    comb = 1
    db = {}                                             # {옷 종류 : [옷1, 옷2, ...]} 딕셔너리 생성
    
    for cloth in clothes:
        if cloth[1] in db:
            db[cloth[1]] = db[cloth[1]] + [cloth[0]]
        else:
            db[cloth[1]] = [cloth[0]]

    for category in db:                                 # 옷 종류별 개수 + 1 (안 입은 경우)를 종류별로 곱하기
        comb *= (len(db[category]) + 1)
    
    return comb - 1                                     # 모두 안 입은 경우 빼기

# 다른 사람의 풀이
def solution(clothes):
    clothes_type = {}

    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2                         # 안 입는 경우까지 미리 카운트
        else:
            clothes_type[t] += 1                        # 옷을 직접 넣지 않고 개수만 올림

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1

'''
회고 / TIL
- 딕셔너리에 종류별 옷을 담아서 풀었는데, 실제로 담지 않고 카운트만 해도 풀 수 있었음. 
'''