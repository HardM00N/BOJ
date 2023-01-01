# https://www.acmicpc.net/problem/1541

'''
나의 접근 / 알고리즘
1. -를 만났을 때, 뒤에 있는 연산자를 -로, 
2. 다시 -를 만나도, 뒤에 있는 연산자를 -로 하면 최소
'''

# 나의 풀이 (Python3 36ms)
exps = input()                                                  # 수식 받기
new_exp = ''                                                    # 수정된 수식

is_minus = False                                                # -가 나온 적이 있는지 체크

for exp in exps:
    if exp == '+':                                              # +가 들어왔을 때
        if is_minus:                                            # 앞에 -가 온 적 있다면
            new_exp += '-'                                      # -로 처리 (분배 법칙)
        else:                                                   # 앞에 -가 온 적 없다면
            new_exp += exp                                      # + 그대로 처리
    
    elif exp == '-':                                            # -가 들어왔을 때
        is_minus = True                                         # 체크
        new_exp += exp
    
    elif exp == '0':                                            # 0이 들어왔을 때
        if new_exp:                                             # 0이 첫 입력이 아니고
            if new_exp[-1] == '-' or new_exp[-1] == '+':        # 수정된 수식의 마지막이 연산자라면
                continue                                        # 해당 0은 의미없으므로 패스
            else:
                new_exp += exp
    
    else:                                                       # +, -, 0이 아니라면
        new_exp += exp                                          # 수정된 수식에 추가

print(eval(new_exp))                                            # str 수식 그대로 연산

# 다른 사람의 풀이
a = input().split('-')                                          # 55, 50+40
r = sum(map(int, a[0].split('+')))                              # 55

for i in range(1, len(a)):
    r -= sum(map(int, a[i].split('+')))                         # 55에서 50+40을 뺌

print(r)

'''
회고 / TIL
- 분배 법칙으로 -를 나눠주기만 하면 최소가 됨. 이를 구현하는 문제였음.
- eval(str)은 str형 수식의 결과를 계산함. 문제를 풀다가 알게 되었음.
- 다른 사람의 풀이를 보니 더 쉽게 풀긴 했지만, 분배 법칙을 구현한다는 것은 같음.
'''