# https://school.programmers.co.kr/learn/courses/30/lessons/86491

# 처음에 생각한 알고리즘
'''
입출력 예 #1
1. 가로나 세로의 max를 찾고, 지갑 크기 초기화 -> 80 x 40
2. max 카드를 제외한 카드 중에서 가로나 세로 중 큰 값으로 정렬-> 70, 60, 60
3. 정렬된 카드의 대응되는 가로나 세로 중 max 값 찾기 -> 30, 50, 30 -> 50
4. 초기화된 지갑 크기보다 크다면, 두 max 값 곱하기 -> 80 x 50 = 4000

입출력 예 #2
1. 15 x 8
2. 15, 14, 12, 10
3. 5, 7, 3, 7 -> 7
4. 15 x 8 = 120

입출력 예 #3
1. 19 x 6
2. 18, 16, 14, 11
3. 7, 6, 4, 7 -> 7
4. 19 x 7 = 133
'''

# 첫 번째 풀이 (테스트 케이스 몇 개 실패)
def solution(sizes):
    x_max = max(map(max, sizes))                    # max 값 찾기
    y_max = 0
    
    for size in sizes:                                  # 앞서 찾은 max 값에 대응하는 가로나 세로 짝 찾기
        if size[0] == x_max:
            if y_max < size[1]:
                y_max = size[1]
        elif size[1] == x_max:
            if y_max < size[0]:
                y_max = size[0]

    try:                                                # 찾은 max 카드 리스트에서 제거
        sizes.remove([x_max, y_max])
    except:
        sizes.remove([y_max, x_max])

    sizes = sum(sizes, [])                              # 남은 리스트 1차원으로
    max_idx = len(sizes) // 2 - 1
    max_candidate = sorted(sizes)[max_idx]              # 정렬했을 때 반으로 나눠 가장 큰 값이 새로운 max 후보

    if y_max < max_candidate:                           # 새로 찾은 max 후보가 기존의 y_max보다 크다면
        y_max = max_candidate
    
    return x_max * y_max                                # 최종 카드 크기 출력

'''
- 테스트 케이스 몇 가지 실패함.
- 반례를 찾아보니 [[91, 50], [77, 51], [50, 1], [50, 50]]일 때 올바른 값이 나오지 않음. 
'''

# 두 번째 풀이 (시간 초과)
def solution(sizes):
    
    x_list, y_list = [], []                             # 가로 혹은 세로의 리스트 생성

    while sizes:                                        # sizes에 카드가 남아있는 한
        sizes_max = max(map(max, sizes))                # 가장 큰 값을 찾고
        
        for size in sizes:                              # 가장 큰 값의 짝도 찾아서
            if size[0] == sizes_max:
                x_list.append(size[0])
                y_list.append(size[1])
                break
            elif size[1] == sizes_max:
                x_list.append(size[1])
                y_list.append(size[0])
                break
        try:                                            # sizes에서 제거하는 것을 반복
            sizes.remove([x_list[-1], y_list[-1]])
        except:
            sizes.remove([y_list[-1], x_list[-1]])

    return max(x_list) * max(y_list)                    # 가로 혹은 세로의 리스트에서 최댓값끼리 곱함

'''
- 첫 번째 풀이에서 간과했던 반례까지 고려해서 재설계함.
- 로직은 정확하나 마지막 테스트 케이스에서 시간 초과 발생함.
'''

# 세 번째 풀이
def solution(sizes):

    x_list, y_list = [], []                             # 가로 혹은 세로의 리스트 생성

    for size in sizes:                                  # sizes를 순회하면서
        if size[0] < size[1]:                           # 큰 값을 x_list에, 작은 값을 y_list에 삽입
            x_list.append(size[1])
            y_list.append(size[0])
        else:
            x_list.append(size[0])
            y_list.append(size[1])

    return max(x_list) * max(y_list)                    # 가로 혹은 세로의 리스트에서 최댓값끼리 곱함.

# 다른 사람의 풀이
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
    # return max(map(max, sizes)) * max(min(x) for x in sizes)가 더 효율적일듯? for문 안 돌아도 되니까...

'''
회고 / TIL
- 세 번째 풀이에서 겨우 문제없이 통과함.
- 카드 크기에서 가로 혹은 세로 여부는 중요하지 않음.
- 반례가 있을 수 있기 때문에, 무턱대고 나열해서 정렬하고 반으로 나누는 식의 풀이는 불가함.
- 두 번째 풀이는 로직은 맞지만 첫 번째 풀이를 베이스로 수정하다보니 굉장히 시간복잡도가 높았음.
- 세 번째 풀이로 통과하고 나니 그리 어렵게 생각할 문제는 아니었던 것 같음.
- 다른 사람의 풀이는 내 세 번째 풀이를 컴프리헨션으로 구현함...
- 처음에 고안한 알고리즘에 갇혀 시간을 많이 소모한 것 같음.
'''