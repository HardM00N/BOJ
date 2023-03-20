# https://school.programmers.co.kr/learn/courses/30/lessons/87390

# 나의 풀이
def solution(n, left, right):
    array = []
    
    for i in range(left, right + 1):
        array.append(max(i // n, i % n) + 1)    # x, y 좌표 중 큰 값에 + 1

    return array

'''
1 2 3
2 2 3
3 3 3

-> 1 2 3 / 2 2 3 / 3 3 3

1 2 3 4
2 2 3 4
3 3 3 4
4 4 4 4

-> 1 2 3 4 / 2 2 3 4 / 3 3 3 4 / 4 4 4 4

- x, y 좌표 중 큰 것을 기준으로 1 더한 값임.
- array[x][y] = max(x, y) + 1

0  1  2  3
4  5  6  7
8  9  10 11
12 13 14 15

- 위 인덱스를 x, y 좌표로 나타내기만 하면 됨.
'''

'''
회고 / TIL
- 다른 사람의 풀이도 비슷함. 
- 1차원 배열의 인덱스를 x, y 좌표로 표현할 수 있으면 풀 수 있음.
'''