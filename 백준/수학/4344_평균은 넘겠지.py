# https://www.acmicpc.net/problem/4344

# 나의 풀이 (Python3 48ms)
for _ in range(int(input())):
    scores = list(map(int, input().split()))
    avg = sum(scores[1:]) / scores[0]                               # 평균 계산
    
    above_avg = [num for num in scores[1:] if num > avg]            # 평균보다 높은 점수 리스트
    print('{:.3f}%'.format(len(above_avg) / scores[0] * 100))       # 비율 계산해 출력

'''
회고 / TIL
- 대체로 풀이들이 비슷해서 다른 사람의 풀이는 생략함. 
- 문자열 포맷팅이 오히려 헷갈려서 애먹었음.
'''