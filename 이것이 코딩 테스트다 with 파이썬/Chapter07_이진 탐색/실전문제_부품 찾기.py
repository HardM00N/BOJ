'''
동빈이네 전자 매장에는 부품이 N개 있다. 
각 부품은 정수 형태의 고유한 번호가 있다. 

어느 날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다. 
동빈이는 때를 놓치지 않고 손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다.

이 때 손님이 요청한 부품 번호의 순서대로 부품을 확인해 부품이 있으면 yes, 
없으면 no를 출력한다. 구분은 공백으로 한다.
'''
# 내 풀이
_ = int(input())
stocks = list(map(int, input().split()))

_ = int(input())
parts = list(map(int, input().split()))

for part in parts:
    cnt = 0
    for stock in stocks:
        if part == stock:
            print('yes', end=' ')
            cnt += 1
            break
    if cnt == 0:
        print('no', end=' ')

# 답안 예시 (이진 탐색)
# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         # 찾은 경우 중간점 인덱스 반환
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None

# for part in parts:
#     result = binary_search(stocks, part, 0, n - 1)
#     if result != None:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')

# 답안 예시 (계수 정렬)
# n = int(input())
# array = [0] * 1000001

# # 가게에 있는 전체 부품 번호를 입력받아 기록
# for i in input().split():
#     array[int(i)] = 1

# # M(손님이 확인 요청한 부품 개수)을 입력 받기
# m = int(input())
# # 손님이 확인 요청한 전체 부품 번호를 공백으로 구분해 입력
# x = list(map(int, input().split()))

# for i in x:
#     if array[i] == 1:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')

# 답안 예시 (집합 자료형 활용)
# n = int(input())
# array = set(map(int, input().split()))

# m = int(input())
# x = list(map(int, input().split()))

# for i in x:
#     if i in array:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')

'''
회고 / TIL
- 나는 문제 그대로 단순히 반복해서 풀었다. 
- 정렬이 되어 있지 않아서 이진 탐색으로 풀지 않았는데, 풀이에서는 그냥 정렬하고 이진 탐색으로 풀더라...
- 계수 정렬과 집합 자료형 활용 풀이는 생각지 못했다. 계수 정렬은 몇 번 봤는데도 잘 안 떠오르는 것 같다. 
'''