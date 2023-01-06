# https://www.acmicpc.net/problem/1065

# 나의 풀이 (Python3 36ms)
N = int(input())
cnt = 0

for i in range(1, N + 1):                                           # 1부터 N까지
    num = str(i)                                                    # str형으로 변환

    for j in range(len(num) - 1):                                   # str의 각 자리를 돌면서 등차수열 체크
        if j == 0:
            gap = int(num[j]) - int(num[j + 1])
        else:
            if gap != int(num[j]) - int(num[j + 1]):                # 등차수열이 아니라면 종료
                break
    else:                                                           # 등차수열이라면 카운트
        cnt += 1

print(cnt)

# 다른 사람의 풀이
def func(a):
    if(a < 100):                                                    # 100 미만은 어차피 한수
        return a
    else:
        x = 99
        for i in range(100, a + 1):
            
            if(int(i / 100) + i % 10 == 2 * (int(i / 10) % 10)):    # 100 이상만 등차수열 체크
                x = x + 1
        return x

x = int(input())
print(func(x))

'''
회고 / TIL
- str형으로 변환해 각 자리의 수를 비교해 등차수열 여부를 체크해서 풀었음.
- 대체로 비슷한 로직임.
'''