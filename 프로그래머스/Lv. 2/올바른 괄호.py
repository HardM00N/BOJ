# https://school.programmers.co.kr/learn/courses/30/lessons/12909

# 첫 번째 풀이 (효율성 테스트 시간 초과)
def solution(s):
    ls = len(s)

    if ls % 2:                                  # s의 길이가 홀수라면
        return False                            # 올바른 괄호가 아님

    ls //= 2                                    # s의 길이가 짝수라면 길이를 2로 나눔 (()) -> 4 // 2 = 2\

    while ls != 0:                              # 2로 나눈 길이만큼 반복하면서
        s = s.replace('()', '')                 # ()을 공백으로 치환

        if not s:                               # 반복 중 s가 모두 공백이 되면 리턴
            return True

        ls -= 1

    if s:                                       # 반복이 끝났음에도 s가 남아있다면 불완전한 괄호
        return False

# 두 번째 풀이 (기준 변수 활용)
def solution(s):
    center = 0                                  # 기준이 되는 변수 선언

    for i in s:
        if center < 0:                          # 음수라면 ')'만 존재한다는 것이므로 불완전한 괄호
            break

        if i == '(':                            # 열린 괄호일 경우 1 더하기
            center += 1
        else:                                   # 닫힌 괄호일 경우 1 빼기
            center -= 1

    return center == 0                          # 반복문의 결과가 0이라면 올바른 괄호

# 세 번째 풀이 (스택 활용)
def solution(s):
    stack = []                                  # 스택 선언

    for i in s:
        if i == '(':                            # 열린 괄호 append
            stack.append(i)
        else:
            if stack and stack[-1] == '(':      # 닫힌 괄호는 스택이 비어있지 않고, top이 열린 괄호일 경우에만
                stack.pop()                     # top의 열린 괄호 제거
            else:
                return False

    if not stack:                               # 반복문이 끝났을 때, stack이 완전히 비어야 올바른 괄호
        return True

    return False                                # stack이 비지 않았다면 (ex. '((((') 불완전한 괄호

'''
회고 / TIL
- 처음에 replace()로 풀었는데, 정답은 맞으나 while 반복문 때문에 효율성 테스트에서 시간 초과가 발생함.
- 두 번째 풀이는 문제 분류가 스택 / 큐이길래 스택으로 풀기 싫은 심보가 발동해 변수 하나를 사용해 올바른 괄호인지 체크해서 풀었음. (다른 사람 풀이와 거의 같음)
- 세 번째 풀이는 심심해서 전형적인 스택으로 풀었음.
'''