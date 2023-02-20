# https://school.programmers.co.kr/learn/courses/30/lessons/12985

'''
                1
       1                  2
   1       2        3           4
 1   2   3   4   5     6     7     8
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
'''
# 나의 풀이
import math

def solution(n, a, b):
    start = 0
    
    while n >= 2:
        if a <= start + n // 2:                         # a가 왼쪽 덩어리냐
            if b <= start + n // 2:                     # b도 왼쪽 덩어리냐
                n //= 2
            
            else:                                       # b는 오른쪽 덩어리냐
                return int(math.log2(n))                # 그럼 지금 바로 최종 라운드에서 만나!
        
        elif a > start + n // 2:                        # a가 오른쪽 덩어리냐
            if b <= start + n // 2:                     # b는 왼쪽 덩어리냐
                return int(math.log2(n))                # 그럼 지금 바로 최종 라운드에서 만나!
            
            else:                                       # b도 오른쪽 덩어리냐
                n //= 2                                 
                start += n                              # 오른쪽 덩어리 선택 시 인덱스 올려주기

# 다른 사람의 풀이
def solution(n, a, b):
    return ((a - 1)^(b - 1)).bit_length()               # XOR 연산으로 거리 비교

'''
회고 / TIL
- 오른쪽 왼쪽으로만 구분해서 라운드가 역순으로 카운팅되도록 풀었음.
- XOR 풀이는 이진 토너먼트이기 때문에 가능한 풀이
'''