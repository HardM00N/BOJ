# https://school.programmers.co.kr/learn/courses/30/lessons/12951

# 나의 풀이
def solution(s):
    result = []
    
    words = s.split(' ')                                                # 공백 기준으로 split

    for word in words:
        if not word:                                                    # ''일 경우
            result.append('')
            continue

        if word[0].isdigit():                                           # 단어의 첫 글자가 숫자라면
            result.append(word[0] + word[1:].lower())
        else:                                                           # 단어의 첫 글자가 알파벳이라면
            result.append(word[0].upper() + word[1:].lower())

    return ' '.join(result)                                             # 본래의 공백들 복원

'''
회고 / TIL
- 공백 기준으로 split하고 그 결과 나오는 ''도 result에 추가해 ' '.join(result)로 단어 사이의 공백들을 복원했음.
- 다른 사람의 풀이들은 문제 개편 전의 풀이들이라 비교하기 애매함.
'''