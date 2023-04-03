# https://school.programmers.co.kr/learn/courses/30/lessons/176963

# 나의 풀이
def solution(name, yearning, photos):
    res = []
    dic = {}
    
    for a, b in zip(name, yearning):            # name:yearning 형태의 딕셔너리 생성
        dic[a] = b
    
    for photo in photos:                        # 사진을 하나씩 가져와서
        temp = 0
        
        for p in photo:                         # 사진 속 이름이 딕셔너리에 있다면 yearning 누적
            if p in dic:
                temp += dic[p]
        
        res.append(temp)

    return res

# 다른 사람의 풀이
def solution(name, yearning, photo):
    dictionary = dict(zip(name,yearning))       # 반복문 없이 바로 딕셔너리 생성
    scores = []
    
    for pt in photo:
        score = 0
        
        for p in pt:
            if p in dictionary:
                score += dictionary[p]
        
        scores.append(score)

    return scores

'''
회고 / TIL
- 딕셔너리로 쉽게 풀 수 있는 문제
- 나는 zip과 for 반복문으로 딕셔너리를 만들었는데, 다른 사람의 풀이를 보니 그렇게 하지 않아도 됨.
'''