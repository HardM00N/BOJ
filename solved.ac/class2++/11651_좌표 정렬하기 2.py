'''
2차원 평면 위의 점 N개가 주어진다. 
좌표를 y 좌표가 증가하는 순으로, y 좌표가 같으면 x 좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오. 
'''

coords = []
for _ in range(int(input())):
    coords.append(list(map(int, input().split())))

coords.sort(key=lambda x: (x[1], x[0]))

for coord in coords:
    print(coord[0], coord[1], sep=' ')

'''
회고 / TIL
- 어제 풀었던 좌표 정렬하기 문제랑 x, y 순서만 바뀐 문제임. 
'''