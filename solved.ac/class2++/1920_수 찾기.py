'''
N개의 정수 A[1], A[2], ..., A[N]이 주어져 있을 때, 
이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오. 
'''
_ = input()
s1 = set(input().split())
_ = input()
l1 = list(input().split())

for num in l1:
    if num in s1:
        print(1)
    else:
        print(0)

'''
회고 / TIL
- set의 in을 이용해서 쉽게 풀었음. 
'''