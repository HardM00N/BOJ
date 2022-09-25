'''
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오. 
'''
nums = []
for _ in range(int(input())):
    nums.append(int(input()))
nums.sort()
for num in nums:
    print(num)

'''
회고 / TIL
- 이번에도 쉽게 정렬은 안 되겠지~ 라는 생각에 일단 그냥 풀었는데 풀리네?
- 뭐지 ???
'''