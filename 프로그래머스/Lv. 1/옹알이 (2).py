# https://school.programmers.co.kr/learn/courses/30/lessons/133499

# 나의 풀이
def solution(babbling):
    rule = set(['aya', 'ye', 'woo', 'ma'])              # 발음할 수 있는 세트
    cnt = 0

    for word in babbling:
        
        temp = ''                                       # 연속된 단어 체크를 위해 이전 단어 저장
        
        while 1:
            
            if word[:2] in rule:                        # 앞 두 글자가 세트에 있으면

                if temp == word[:2]:                    # 연속된 단어였다면 break
                    break
                
                temp = word[:2]
                word = word[2:]                         # 남은 단어 갱신
            
            elif word[:3] in rule:                      # 앞 세 글자가 세트에 있으면

                if temp == word[:3]:                    # 연속된 단어였다면 break
                    break

                temp = word[:3]
                word = word[3:]                         # 남은 단어 갱신
            
            else:
                break
            
            if not word:                                # word가 비었다면
                cnt += 1                                # 발음할 수 있는 것들로만 이루어졌다는 뜻이므로 카운트
                break
    
    return cnt

# 다른 사람의 풀이
def solution(babbling):
    count = 0

    for b in babbling:
        if "ayaaya" in b or "yeye" in b or "woowoo" in b or "mama" in b:                                                # 발음이 연속된 경우를 미리 필터링
            continue    
        if not b.replace("aya", " ").replace("ye", " ").replace("woo", " ").replace("ma", " ").replace(" ", ""):        # 모두 replace한 결과가 공백이라면 카운트
            count += 1

    return count

'''
회고 / TIL
- 슬라이싱으로 단어를 잘라서 비교하다가 단어의 길이가 0이 되면 카운트하는 식으로 풀었음.
- replace를 이용한 다른 사람의 풀이... 똑똑하다...
'''