'''
하나의 수열에는 다양한 수가 존재한다. 
이러한 수는 크기에 상관없이 나열되어 있다. 
이 수를 큰 수부터 작은 수의 순서로 정렬해야 한다. 
수열을 내림차순으로 정렬하는 프로그램을 만드시오.
'''
# 내 풀이

N = int(input())
nums = []

for _ in range(N):
    nums.append(int(input()))

nums.sort(reverse=True)

for num in nums:
    print(nums, end=' ')

'''
회고 / TIL
- 기본 정렬 문제라 답안 예시와 거의 비슷했음. 
- 이런 문제만 나오면 얼마나 좋을까. 
'''