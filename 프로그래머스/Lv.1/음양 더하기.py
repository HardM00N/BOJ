# https://school.programmers.co.kr/learn/courses/30/lessons/76501

# 나의 풀이
def solution(absolutes, signs):
    
    for idx, sign in enumerate(signs):
        if not sign:                        # 부호가 음수면
            absolutes[idx] *= -1            # 숫자를 음수로

    return sum(absolutes)

# 다른 사람의 풀이
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))

'''
회고 / TIL
- 푸는 로직은 모두 비슷함. 
- 저런 한 줄로 푸는 스킬이 아직 부족함.
'''