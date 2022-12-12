# https://school.programmers.co.kr/learn/courses/30/lessons/12918

# 나의 풀이
def solution(s):
    if len(s) == 4 or len(s) == 6:              # 길이가 4나 6이고
        try:
            s = int(s)                          # 숫자로만 이루어져있으면
            return True
        except:                                 # 문자가 섞여있어서 에러가 나면
            return False
    else:
        return False                            # 길이가 4나 6이 아니면

# 다른 사람의 풀이
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)     # 숫자로만 이루어져있고 길이가 4나 6인지

'''
회고 / TIL
- 숫자를 판별하기 위해 int 변환과 try except 구문을 사용함. 
- 다른 사람의 풀이를 보니 str이 숫자로만 이루어졌는지 판별하는 isdigit()이 있었다... 
'''