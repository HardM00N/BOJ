'''
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오. 
'''

_ = input()
nums = list(map(int, input().split()))
total = 0

for num in nums:
    cnt = 0
    for i in range(1, num + 1):
        if num % i == 0:
            cnt += 1
    if cnt == 2:
        total += 1

print(total)

'''
회고 / TIL
- 하나하나 나눠보면서 1과 자기자신으로만 나누어지는지 체크해 소수 판별하면 됨. 
- 단순히 풀어서 금방 풀었음. 
'''