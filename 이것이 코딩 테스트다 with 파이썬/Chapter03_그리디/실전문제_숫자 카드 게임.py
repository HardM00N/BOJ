'''
숫자 카드 게임은 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임임. 

단, 게임의 룰을 지키며 카드를 뽑아야 하고 룰은 다음과 같음. 

1. 숫자가 쓰인 카드들이 N x M 형태로 놓여 있다. N은 행의 개수, M은 열의 개수를 의미함. 
2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택함. 
3. 그 다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 함. 
4. 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려해 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있는 전략을 세워야 함. 

카드들이 N x M 형태로 놓여 있을 때, 게임의 룰에 맞게 카드를 뽑는 프로그램을 만드시오.
'''

# min() 함수를 이용하는 답안 예시
n, m = map(int, input().split())

result = 0

# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))

    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)   # 최종 답안 출력

# 2중 반복문 구조를 이용하는 답안 예시
n, m = map(int, input().split())

result = 0

# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))

    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)   # 최종 답안 출력

'''
회고 / TIL
- 문제를 이해하는데 시간이 오래 걸렸음. (왜 작은 수들 중에서 큰 수를 뽑는지)
- 일단 가장 작은 수를 다 뽑고, 그 중에서 큰 수를 뽑는 방향으로 접근하기에 그리디 유형인 것 같음. 
- 문제만 이해하면 어렵지 않게 풀 수 있는 문제임. 
'''