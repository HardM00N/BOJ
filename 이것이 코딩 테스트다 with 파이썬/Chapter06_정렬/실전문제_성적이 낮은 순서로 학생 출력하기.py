'''
N명의 학생 정보가 있다. 
학생 정보는 학생의 정보와 학생의 성적으로 구분된다. 
각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오.
'''
students = []

for _ in range(int(input())):
    name, score = input().split()
    students.append((name, int(score)))

students = sorted(students, key=lambda x: x[1])

for student in students:
    print(student[0], end=' ')

'''
회고 / TIL
- 풀고 보니 예시 답안이랑 굉장히 비슷함. 
- sorted에서 key 사용하는 부분은 헷갈려서 사용법을 검색했다. 
'''