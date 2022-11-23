# https://www.acmicpc.net/problem/4673

# 나의 풀이 (Python3 620ms / PyPy3 156ms)
d_list = []                         # d(n)의 결과를 저장할 리스트

for i in range(1, 10001):           # 1부터 10000까지 d(n) 계산
    d_sum = i                       # d(n)은 n과 n의 각 자릿수의 합이므로, d_sum에 우선 i를 더하고
    i = str(i)                      # i의 자릿수만큼 반복하면서 d_sum에 각 자리의 값을 더함.
    for j in range(len(i)):
        d_sum += int(i[j])

    d_list.append(d_sum)            # 계산된 d(n)의 결과를 d_list에 저장

for i in range(1, 10001):           # 1부터 10000까지 돌면서
    if i in d_list:                 # 만약 i가 d_list에 있다면, 생성자가 있다는 뜻이므로 건너뜀. 
        continue    
    print(i)                        # 그렇지 않다면, 셀프 넘버이므로 출력