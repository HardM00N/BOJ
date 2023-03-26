# https://school.programmers.co.kr/learn/courses/30/lessons/92335

# 나의 풀이
def solution(n, k):
    n_number = ''                                       # n진수 변환

    while n > 0:
        n, mod = divmod(n, k)
        n_number += str(mod)

    n_list = n_number[::-1].split('0')                  # 변환된 n진수를 0 기준으로 스플릿
    
    cnt = 0

    for i in n_list:                                    # 스플릿된 리스트를 돌며 소수 체크
        if not i:                                       # 스플릿된 결과가 ''인지
            continue

        i = int(i)

        if i == 1:                                      # 스플릿된 결과가 1인지
            continue

        for j in range(2, int(i ** 0.5) + 1):           # 소수 체크
            if i % j == 0:
                break
        else:
            cnt += 1
    
    return cnt

'''
회고 / TIL
- 되게 지저분하게 풀었다고 생각했는데, 다른 사람들의 풀이도 대체로 길이가 비슷함.
- 이런 문제는 소수 체크, n진수 변환 부분을 함수화하는 것이 바람직하다고 생각됨.
'''