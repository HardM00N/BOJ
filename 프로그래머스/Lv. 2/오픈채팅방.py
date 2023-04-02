# https://school.programmers.co.kr/learn/courses/30/lessons/42888

# 나의 풀이
def solution(record):
    uid_dict = {}
    res = []

    for r in record:                                        # uid - aka 딕셔너리 생성
        if len(r.split()) == 3:
            _, uid, aka = r.split()
            uid_dict[uid] = aka

    for r in record:                                        # 생성한 딕셔너리 토대로 답 출력
        if len(r.split()) == 3:
            action, uid, _ = r.split()
        else:
            action, uid = r.split()

        if action == 'Enter':
            res.append(uid_dict[uid] + '님이 들어왔습니다.')
        elif action == 'Leave':
            res.append(uid_dict[uid] + '님이 나갔습니다.')
    
    return res

# 다른 사람의 풀이
def solution(record):
    user_id = {EC.split()[1]:EC.split()[-1] for EC in record if EC.startswith('Enter') or EC.startswith('Change')}
    return [f'{user_id[E_L.split()[1]]}님이 들어왔습니다.' if E_L.startswith('Enter') else f'{user_id[E_L.split()[1]]}님이 나갔습니다.' for E_L in record if not E_L.startswith('Change')]

'''
회고 / TIL
- 문제에 입각한 정직한 풀이
- 다른 사람의 풀이는 startswith를 활용함.
'''