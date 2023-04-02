# https://school.programmers.co.kr/learn/courses/30/lessons/160586

# 나의 풀이
def make_keydict(keymap):                   # keymap에서 문자마다 필요한 최소횟수를 저장하는 딕셔너리 생성 
    keydict = {}

    for key in keymap:
        for i, k in enumerate(key):
            if k in keydict:                # 딕셔너리에 이미 문자 k가 있다면
                if i + 1 < keydict[k]:      # 더 작은 횟수 (최소횟수)를 딕셔너리에 저장
                    keydict[k] = i + 1
            else:                           # 딕셔너리에 문자 k가 없었다면 추가
                keydict[k] = i + 1

    return keydict

def solution(keymap, targets):

    keydict = make_keydict(keymap)          # keymap으로부터 딕셔너리 생성
    result = []

    for target in targets:
        cnt = 0

        for t in target:
            if t not in keydict:            # 누를 수 없는 문자라면
                result.append(-1)           # result에 -1 추가하고 break
                break
            cnt += keydict[t]
        
        else:                               # break 없이 for문이 모두 돌았다면 (for - else)
            result.append(cnt)              # 누른 횟수 result에 append

    return result

'''
회고 / TIL
- keymap의 여러 key들로부터 각 문자마다 눌러야할 최소 횟수가 담긴 딕셔너리를 생성하는게 중요한 문제였음.
- 다른 사람의 풀이도 큰 틀에서 보면 비슷했음.
'''