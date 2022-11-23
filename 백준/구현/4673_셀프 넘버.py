# https://www.acmicpc.net/problem/4673

# 나의 풀이 (Python3 620ms / PyPy3 156ms)
d_list = []                                   # d(n)의 결과를 저장할 리스트

for i in range(1, 10001):                     # 1부터 10000까지 d(n) 계산
    d_sum = i                                 # d(n)은 n과 n의 각 자릿수의 합이므로, d_sum에 우선 i를 더하고
    i = str(i)                                # i의 자릿수만큼 반복하면서 d_sum에 각 자리의 값을 더함.
    for j in range(len(i)):
        d_sum += int(i[j])

    d_list.append(d_sum)                      # 계산된 d(n)의 결과를 d_list에 저장

for i in range(1, 10001):                     # 1부터 10000까지 돌면서
    if i in d_list:                           # 만약 i가 d_list에 있다면, 생성자가 있다는 뜻이므로 건너뜀. 
        continue    
    print(i)                                  # 그렇지 않다면, 셀프 넘버이므로 출력

# 다른 사람의 풀이 (Python3 88ms / PyPy3 120ms)
natural_num = set(range(1, 10001))              # set 자료형으로 1부터 10000까지 생성
generated_num = set()                           # 마찬가지로 set 자료형 선언

for i in range(1, 10001):       
    for j in str(i):                            # for문 선언할 때 str형으로 바꿔서
        i += int(j)                             # 각 자리를 나보다 수월하게 더함.
    generated_num.add(i)                        # 계산된 결과를 앞서 선언한 set에 추가

self_num = sorted(natural_num - generated_num)  # set 간의 - 연산으로 셀프 넘버만 남김. 
for i in self_num:
    print(i)

'''
회고 / TIL
- 10000까지 출력하는 거라서, 시간복잡도에 대한 큰 걱정없이 구현했음. 
- 다른 사람의 풀이를 보니 set 자료형을 사용해서 시간을 획기적으로 줄였음. 
- 요런 문제가 나올 때 set 자료형을 활용하려고 노력해봐야겠음. 
'''