'''
온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 
이 때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로
정렬하는 프로그램을 작성하시오. 
'''

datas = []
for _ in range(int(input())):
    datas.append(list(input().split()))

datas.sort(key = lambda x: int(x[0]))

for data in datas:
    print(data[0], data[1])

'''
회고 / TIL
- 단순한 정렬 문제였음.
- 이미 list에는 순서대로 index가 부여되므로, 나이로만 정렬해주면 같은 나이에 대해서는 index 순서가 적용됨. 
- sort에 lambda 함수는 아직도 손에 완전히 붙질 않았음. 
'''