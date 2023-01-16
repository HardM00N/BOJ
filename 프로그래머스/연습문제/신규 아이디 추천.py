# https://school.programmers.co.kr/learn/courses/30/lessons/72410

# 나의 풀이
import re

def solution(new_id):
    new_id = re.sub(r"[^a-z0-9-_.]", "", new_id.lower())                                            # 소문자화 및 숫자, 특문 -_.만 남기고 제거
    new_id = re.sub('[\.]+', '.', new_id)                                                           # 반복되는 ... 하나의 .으로 대체

    if new_id and new_id[0] == '.':                                                                 # 앞 뒤의 . 제거
        new_id = new_id[1:]
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]

    if not new_id:                                                                                  # id가 비었으면
        new_id += 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    if len(new_id) <= 2:
        new_id += new_id[-1] * (3 - len(new_id))
    
    return new_id

# 다른 사람의 풀이2
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)                                                                # 앞 뒤의 . 제거
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st

'''
회고 / TIL
- 앞 뒤의 .을 제거하는 방법을 몰라 슬라이싱으로 제거함... 정규식 공부하자!
- 반복되는 ...을 하나의 .으로 만드는 방법도 구글링함...
'''