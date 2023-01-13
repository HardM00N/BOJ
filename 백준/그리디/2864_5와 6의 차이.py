# https://www.acmicpc.net/problem/2864

# 나의 풀이 (Python3 32ms)
A, B = input().split()

a5, b5 = A.replace('6', '5'), B.replace('6', '5')           # 모든 6을 5로
a6, b6 = A.replace('5', '6'), B.replace('5', '6')           # 모든 5를 6으로

print(int(a5) + int(b5), int(a6) + int(b6))


# 다른 사람의 풀이
a = input().replace(' ', '+').replace('6', '5')             # 한 번에 수식으로 바꾸고
print(eval(a), eval(a.replace('5', '6')))                   # eval()로 연산

'''
회고 / TIL
- 최대일 경우는 모든 5를 6으로 혼동했을 때, 최소일 경우는 반대임.
'''