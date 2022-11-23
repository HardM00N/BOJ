# https://www.acmicpc.net/problem/1316

# 나의 풀이 (Python3 136ms / PyPy3 200ms)
from string import ascii_lowercase

cnt = 0                                     # 그룹 단어 카운트
words = []

for _ in range(int(input())):
    words.append(input())

for word in words:
    a_to_z = set(ascii_lowercase)           # 소문자 알파벳 set 생성
    tmp = ''                                # 연속된 알파벳을 확인하기 위한 변수
    
    for character in word:                  # 주어진 문자열의 각 글자를 돌며
        if character in a_to_z:             # 1. 알파벳 set에 있는지 (전에 나왔던 알파벳이라면 set에 없을 것임)
            a_to_z.remove(character)        # 처음 나온 알파벳이라면 set에서 제거
            tmp = character                 # tmp에 현재 알파벳 저장
        elif character == tmp:              # 2. 처음 나온 알파벳은 아니지만 이전 알파벳과 같다면
            pass                            # 아무것도 하지 않음
        else:
            break                           # 위 조건 모두 불만족 시 break
    else:
        cnt += 1                            # for-else 문으로 위 for문이 정상적으로 모두 수행되었다면, 그룹 단어이므로 카운트

print(cnt)