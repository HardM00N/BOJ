# https://school.programmers.co.kr/learn/courses/30/lessons/42885

# 첫 번째 풀이 (효율성 테스트 4, 5 실패)
def solution(people, limit):
    
    people = sorted(people)                         # 오름차순 정렬
    len_p = len(people)                             # 리스트 길이
    cnt, tmp = 0, 1                                 # cnt : 조건의 맞는 짝 카운트, tmp: 뒤에서부터 탐색할 인덱스

    for i in range(len_p):
        if tmp == -len_p:                           # 왼쪽 인덱스 i와 오른쪽 인덱스 tmp의 교차 방지
            break
        
        for j in range(tmp, len_p - i):             # tmp는 뒤에서부터 탐색
            if people[i] + people[-j] <= limit:     # 조건에 맞는 짝을 찾으면
                tmp = j + 1                         # 다음 tmp 위치 갱신
                cnt += 1
                break

    return len_p - cnt

# 두 번째 풀이
def solution(people, limit):
    
    people = sorted(people)
    len_p = len(people)
    cnt, tmp = 0, 1

    for i in range(len_p):
        if tmp == -len_p:
            break
        
        for j in range(tmp, len_p - i):
            if people[i] + people[-j] <= limit:
                tmp = j + 1
                cnt += 1
                break
        else:                                       # 추가
            break                                   # 추가

    return len_p - cnt

'''
정확성  테스트
테스트 1 〉	통과 (1.19ms, 10.3MB)
테스트 2 〉	통과 (0.54ms, 10.1MB)
테스트 3 〉	통과 (0.85ms, 10.1MB)
테스트 4 〉	통과 (0.81ms, 10.1MB)
테스트 5 〉	통과 (0.47ms, 10.2MB)
테스트 6 〉	통과 (0.23ms, 10.1MB)
테스트 7 〉	통과 (0.38ms, 10.4MB)
테스트 8 〉	통과 (0.03ms, 10.2MB)
테스트 9 〉	통과 (0.11ms, 10.1MB)
테스트 10 〉	통과 (0.75ms, 10.1MB)
테스트 11 〉	통과 (1.19ms, 10.4MB)
테스트 12 〉	통과 (0.62ms, 10.1MB)
테스트 13 〉	통과 (0.74ms, 10.4MB)
테스트 14 〉	통과 (0.66ms, 10.2MB)
테스트 15 〉	통과 (0.10ms, 10.3MB)

효율성  테스트
테스트 1 〉	통과 (13.80ms, 10.9MB)
테스트 2 〉	통과 (8.83ms, 10.8MB)
테스트 3 〉	통과 (16.62ms, 10.8MB)
테스트 4 〉	통과 (7.25ms, 10.9MB)
테스트 5 〉	통과 (7.63ms, 10.8MB)
'''

'''
회고 / TIL
- 처음에 시간 초과났는데, 딘순히 for문에 else문을 추가해 헛도는거 막으니 바로 풀림. 
- 별생각없이 풀었는데 다른 사람의 풀이를 보니 내가 푼게 투 포인터인듯함. 암튼 그러함.
'''