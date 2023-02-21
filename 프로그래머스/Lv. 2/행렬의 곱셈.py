# https://school.programmers.co.kr/learn/courses/30/lessons/12949

# 나의 풀이
def solution(arr1, arr2):
    res = []

    for i in range(len(arr1)):                      # arr1의 한 행씩 가져오기
        temp = []
        
        for j in range(len(arr2[0])):               # arr2의 한 열씩 가져오기
            total = 0

            for k in range(len(arr1[0])):           # 앞서 가져온 arr1의 한 행의 요소들 * arr2의 한 열의 요소들
                total += arr1[i][k] * arr2[k][j]
            
            temp.append(total)                      # 결과 행렬의 한 행 완성하기
        res.append(temp)                            # 완성된 행들을 append

    return res

# 다른 사람의 풀이
def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
# zip(*B) : [(1, 3, 5), (2, 4, 6)] -> [[1,2], [3,4], [5,6]]

# 다른 사람으 ㅣ풀이
import numpy as np

def productMatrix(A, B):
    return (np.matrix(A)*np.matrix(B)).tolist()     # 이렇게 풀까 고민했는데... ㅋㅋ

'''
회고 / TIL
- 단순 행렬 곱이지만, 구현해보긴 처음임. 생각보다 헷갈려서 애먹었음.
- zip과 *를 이용한 다른 사람의 풀이가 정말 대단함.
- numpy는 웃고 가자.
'''