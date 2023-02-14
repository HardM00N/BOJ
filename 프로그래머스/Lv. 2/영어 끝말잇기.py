# https://school.programmers.co.kr/learn/courses/30/lessons/12981

# 나의 풀이
def solution(n, words):
    word_set = set()                                                        # 중복 체크를 위한 세트
    temp = words[0][0]                                                      # 첫 글자로 temp 초기화

    for i, word in enumerate(words):
        if temp[-1] == word[0] and word not in word_set:                    # 끝말잇기가 맞고, 앞에 나온 적 없는 단어면
            word_set.add(word)                                              # 단어 세트에 추가하고
            temp = word                                                     # temp 갱신
            continue
        else:                                                               # 아닌 경우라면 틀렸으므로
            return [(i + 1) % n if (i + 1) % n else  n, (i // n) + 1]       # 규칙에 따라 리턴

    else:
        return [0, 0]

'''
# 인덱스 규칙
1 0 -> [1, 1]
2 1 -> [2, 1]
3 2 -> [3, 1]
4 3 -> [1, 2]
5 4 -> [2, 2]
6 5 -> [3, 2]
7 6 -> [1, 3]
8 7 -> [2, 3]
9 8 -> [3, 3]

1 0 -> [1, 1]
2 1 -> [2, 1]
3 2 -> [1, 2]
4 3 -> [2, 2]
5 4 -> [1, 3]
6 5 -> [2, 3]
'''

'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.00ms, 10.1MB)
테스트 4 〉	통과 (0.02ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.00ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.1MB)
테스트 13 〉	통과 (0.00ms, 10.3MB)
테스트 14 〉	통과 (0.01ms, 10.1MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.1MB)
테스트 17 〉	통과 (0.00ms, 10.1MB)
테스트 18 〉	통과 (0.01ms, 10.1MB)
테스트 19 〉	통과 (0.01ms, 10.1MB)
테스트 20 〉	통과 (0.04ms, 10.1MB)
'''

# 다른 사람의 풀이
def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]

'''
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.00ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.03ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.03ms, 10.3MB)
테스트 11 〉	통과 (0.03ms, 10.1MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.00ms, 10.2MB)
테스트 16 〉	통과 (0.00ms, 10.2MB)
테스트 17 〉	통과 (0.00ms, 10.2MB)
테스트 18 〉	통과 (0.01ms, 10.2MB)
테스트 19 〉	통과 (0.00ms, 10.1MB)
테스트 20 〉	통과 (0.16ms, 10.3MB)
'''

'''
회고 / TIL
- 문제 자체는 쉬웠으나 리턴하는 값들의 인덱스 계산에서 애먹었음.
- 다른 사람의 풀이는 더 간결하지만 set를 쓰지 않았기 때문에 in 메서드에서 시간이 느림.
'''