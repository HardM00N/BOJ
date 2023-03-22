# https://school.programmers.co.kr/learn/courses/30/lessons/42577

# 첫 번째 풀이 (효율성 테스트 3, 4 시간 초과)
from itertools import combinations

def solution(phone_book):

    for i, j in combinations(sorted(phone_book, key=len), 2):           # 길이 순 정렬 후 조합
        if i == j[:len(i)]:
            return False   
    
    return True

# 두 번째 풀이
def solution(phone_book):
    phone_book.sort()                                                   # 오름차순 정렬

    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False
    
    return True

'''
회고 / TIL
- 접두어니까 길이 순으로 정렬하면 찾기 쉽겠지하고 정직하게 막 풀었다가 효율성 테스트 3, 4 시간 초과남.
- 인접한 요소들끼리 비교하기 위한 최선은 그냥 정렬이었음. 한참 고민했음...
- 다 풀고 창민님 풀이 봤는데 처음부터 일반 정렬로 푸신거보고 깜짝 놀람... 실력자...
'''