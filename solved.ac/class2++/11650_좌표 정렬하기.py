'''
2차원 평면 위의 점 N개가 주어진다. 
좌표를 x 좌표가 증가하는 순으로, x 좌표가 같으면 y 좌표가 증가하는 순서로 정렬해 출력하는 프로그램을 작성하시오. 
'''
coords = []
for _ in range(int(input())):
    coords.append(list(map(int, input().split())))

coords.sort(key=lambda x: (x[0], x[1]))

for coord in coords:
    print(coord[0], coord[1], sep=' ')

'''
회고 / TIL
- sort에 lambda를 활용해 조건을 두 개 적용하면 쉽게 풀림. 
- easy한 문제 아주 좋습니다..
'''