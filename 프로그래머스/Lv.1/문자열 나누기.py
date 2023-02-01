# https://school.programmers.co.kr/learn/courses/30/lessons/140108

# 나의 풀이
def solution(s):
    res = []                                                    # 분리한 문자열 보관
    
    while s:
        if len(s) < 2:                                          # 한 글자만 남았다면 바로 res에 보관하고 종료
            res.append(s)
            break

        x = s[0]                                                # 첫 번째 글자
        y = s[1]                                                # 두 번째 글자

        if x != y:                                              # 다르다면
            res.append(s[:2])                                   # 분리 후 res에 보관
            s = s[2:]                                           # 남은 글자들로 다시 진행
            continue
        
        else:
            cnt_x, cnt_others = 2, 0                            # 같다면

            for i in s[2:]:                                     # 세 번째 글자부터 확인
                if i == x:
                    cnt_x += 1
                else:
                    cnt_others += 1

                if cnt_x == cnt_others:                         # x와 나머지 글자 개수가 같아지면
                    res.append(s[:cnt_x + cnt_others])          # res에 해당 문자열까지 보관
                    s = s[cnt_x + cnt_others:]
                    break
            else:                                               # 문자를 다 돌았는데도 x와 나머지 글자 개수가 같지 않다면 
                res.append(s)                                   # 나머지 전체를 res에 보관하고 종료
                s = ''
        
    return len(res)

# 다른 사람의 풀이
def solution(s):
    answer = 0
    sav1, sav2 = 0, 0
    
    for i in s:
        if sav1 == sav2:
            answer += 1                                         # 처음에 카운트하고 시작
            a = i
        
        if i == a:
            sav1 += 1
        else:
            sav2 += 1
    
    return answer

'''
회고 / TIL
- 쉬운 문제였는데 되게 복잡하게 풀었음. 이런 일이 잦은 거 같음...
- 굳이 문자열을 실제로 자를 필요 없이, 카운트만 적절히 해주면 됨.
'''