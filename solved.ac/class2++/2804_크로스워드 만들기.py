'''
창영이는 크로스워드 퍼즐을 만들려고 한다.

두 단어 A와 B가 주어진다. 
A는 가로로 놓여야 하고, B는 세로로 놓여야 한다. 
또, 두 단어는 서로 교차해야 한다. (정확히 한 글자를 공유해야 한다)
공유하는 글자는 A와 B에 동시에 포함되어 있는 글자여야 하고, 그런 글자가 여럿인 경우 A에서 제일 먼저 등장하는 글자를 선택한다. 
마찬가지로 이 글자가 B에서도 여러 번 등장하면 B에서 제일 처음 나오는 것을 선택한다. 

예를 들어, A = "ABBA"이고, B = "CCBB"라면, 아래와 같이 만들 수 있다.
'''

a, b = input().split()

for i in a:
    if i in b:
        check = i
        break
where_a = a.index(check)
where_b = b.index(check)

for i in range(len(b)):
    for j in range(len(a)):
        if i == where_b:
            print(a)
            break
        if j == where_a:
            if j == len(a) - 1:     # 요 조건이 없어서 틀리신 듯?
                print(b[i])         # 공유하는 글자가 열의 마지막에 올 경우에 대한 예외 처리 (개행)
            else:                   
                print(b[i], end='')
        elif j == len(a) - 1:
            print('.')
        else:
            print('.', end='')

'''
회고 / TIL
- 내가 풀던 문제는 아니었고, 창민님이 코드 오류를 찾아달라고 해서 보게 된 문제임. 
- 창민님 코드에서 조건 하나만 추가해서 해결함. (겹치는 문자가 마지막 열에 있을 경우에 대한 예외 처리가 없었음)
- 개인적으로 다시 풀어볼 예정임. 
'''