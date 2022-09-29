'''
요세푸스 문제는 다음과 같다. 

1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(<=N)가 주어진다. 
이제 순서대로 K번째 사람을 제거한다. 

한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 
이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 

원에서 사람들이 제거되는 순서를 (N, K) - 요세푸스 순열이라고 한다. 
예를 들어 (7, 3) - 요세푸스 순열은 < 3, 6, 2, 7, 5, 1, 4 > 이다. 
'''

N, K = map(int, input().split())
data = list(x for x in range(1, N + 1))
results = []
index = 0

while data:
    index += (K - 1)
    if index >= len(data):  # index가 범위를 벗어나면
        index %= len(data)  # 리스트 길이만큼 나눈 나머지를 index로 사용
    results.append(data.pop(index))

print('<' + str(results)[1:-1] + '>')


# print('<', end='')
# for result in results:
#     if results.index(result) == len(results) - 1:
#         print(result, end='>')
#     else:
#         print(result, end=', ')

'''
회고 / TIL
- 구현 자체는 어렵지 않았음. index 범위만 잘 설정해주면 됨. 
- 오히려 결과를 출력하는 부분이 더 까다로웠음. 더 효율적인 방법이 있을 것 같음. 
- 다른 사람의 풀이를 보니 슬라이싱으로 출력하는 방법이(대단...) 있어서 그렇게 바꿈. 
'''