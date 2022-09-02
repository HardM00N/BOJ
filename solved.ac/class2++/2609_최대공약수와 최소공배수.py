'''
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오. 
'''

n, m = map(int, input().split())

for i in range(min(n, m), 0, -1):
    if n % i == 0 and m % i == 0:
        print(i)                        # 최대 공약수
        print(n * m // i)               # 최소 공배수
        break

# for i in range(max(n, m), (n * m) + 1):
#     if i % n == 0 and i % m == 0:
#         print(i)
#         break

'''
- 다현님 풀이 보고 유클리드 호제법이란 걸 처음 알았다.
- 최대 공약수, 최소 공배수 문제는 기초 수학인데도 코드로 구현할 때는 헷갈린다. 
'''