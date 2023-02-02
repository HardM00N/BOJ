# https://www.acmicpc.net/problem/10610

# 나의 풀이 (Python3 64ms)
N = input()

if sum(list(map(int, N))) % 3 == 0 and '0' in N:        # 각 자릿수의 합이 3의 배수이면서 '0'이 포함되어 있다면 30의 배수이므로
    print(''.join(sorted(N, reverse=True)))             # 가장 큰 수가 왼쪽으로 오도록 내림차순 정렬해서 출력
else:
    print(-1)                                           # 30의 배수가 아니라면 -1 출력

'''
회고 / TIL
- 3의 배수는 각 자릿수의 합이 3의 배수라는 특징을 미리 알고 있었기에 쉽게 풀었음.
- 3의 배수더라도 30의 배수가 되려면 숫자 '0'을 포함해야 하므로 이를 이용하면 매우 쉽게 풀림.
- 다른 사람의 풀이들도 비슷함. 
'''