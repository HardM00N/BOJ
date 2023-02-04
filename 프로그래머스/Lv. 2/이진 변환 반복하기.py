# https://school.programmers.co.kr/learn/courses/30/lessons/70129

# 나의 풀이
def solution(s):
    answer = [0, 0]

    while s != '1':                             # s가 '1'이 되면 종료
        answer[0] += 1                          # 이진 변환 카운트
        answer[1] += s.count('0')               # 제거될 0의 개수 카운트

        s = str(bin(s.count('1'))[2:])          # 1만 남았을 때의 길이를 이진 변환 후 str()

    return answer

'''
회고 / TIL
- 오랜만에 보는 이진 변환 문제 (bin(), hex(), oct(), int() 등을 기억하자)
- 다른 사람의 풀이도 비슷함.
'''