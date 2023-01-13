# https://www.acmicpc.net/problem/1292

# 나의 풀이 (Python3 36ms)
A, B = map(int, input().split())

nums = [0]
num, idx = 1, 1

while idx <= 1000:                              # 1000개까지 nums 채우기
    for k in range(num):
        nums.append(num)
        idx += 1
    num += 1

print(sum(nums[A:B + 1]))                       # 완성된 nums에서 슬라이싱해 합산

'''
회고 / TIL
- 수열을 만드는게 까다로웠음.
'''