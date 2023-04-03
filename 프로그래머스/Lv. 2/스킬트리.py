# https://school.programmers.co.kr/learn/courses/30/lessons/49993

# 나의 풀이
def solution(skill, skill_trees):
    skill_set = set(skill)              # in 메서드를 빠르게 쓰기 위한 스킬 세트 생성
    cnt = 0

    for skill_tree in skill_trees:      # 스킬 트리를 돌면서
        temp = ''
        for s in skill_tree:            # 스킬이 스킬 세트에 있다면
            if s in skill_set:
                temp += s               # temp에 해당 스킬을 추가
        
        if skill.startswith(temp):      # 스킬트리가 temp로 시작된다면 순서가 지켜졌으므로
            cnt += 1                    # 카운트

    return cnt

'''
회고 / TIL
- 순서를 지켜야 할 스킬들을 제외하고는 모두 제거한 후, 남아있는 스킬들이 순서를 지키고 있는지 startswith로 체크함.
'''