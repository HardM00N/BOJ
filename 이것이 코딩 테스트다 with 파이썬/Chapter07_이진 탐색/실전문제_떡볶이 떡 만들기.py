'''
오늘 동빈이는 여행 가신 부모님을 대신해서 떡집 일을 하기로 했다. 
오늘은 떡볶이 떡을 만드는 날이다. 동빈이네 떡볶이 떡은 재밌게도 떡의 길이가 일정하지 않다. 
대신에 한 봉지에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰준다. 

절단기에 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단한다. 
높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다. 

예를 들어 높이가 19, 14, 10, 17cm인 떡이 나란히 있고 절단기 높이를 15cm로 지정하면
자른 뒤 떡의 높이는 15, 14, 10, 15cm가 될 것이다. 
손님은 6cm만큼의 길이를 가져간다. 

손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 
절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.
'''
# 내 풀이
_, _ = map(int, input().split())
heights = list(map(int, input().split()))
max_height = max(heights)

for i in range(max_height, 0, -1):
    sum = 0
    
    for height in heights:
        if height - i < 0:
            continue
        else:
            sum += height - i
    
    if sum >= M:
        print(i)
        break

# 답안 예시
# n, m = list(map(int, input().split(' ')))
# array = list(map(int, input().split()))

# # 이진 탐색을 위한 시작점과 끝점 설정
# start = 0
# end = max(array)

# # 이진 탐색 수행 (반복적)
# result = 0
# while(start <=end):
#     total = 0
#     mid = (start + end) // 2
#     for x in array:
#         # 잘랐을 때의 떡의 양 계산
#         if x > mid:
#             total += x - mid
    
#     # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
#     if total < m:
#         end = mid - 1
#     # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
#     else:
#         result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
#         start = mid + 1

# # 정답 출력
# print(result)

'''
회고 / TIL
- 그냥 단순히 가장 큰 떡의 길이부터 1씩 감소하면서 잘라나가서 자른 나머지의 총합이 M이 되는 지점을 찾게끔 풀었음. 
- 절단기의 높이는 1부터 10억까지의 정수 중 하나이므로, 당연하게 이진 탐색을 사용해야 한다고 한다. 크흠... (귀찮)
- 막상 이진 탐색 코드를 보니 간결해서 손에 익으면 쓸만할 것 같다. 
'''