def solution(survey, choices):

    result = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for question, score in zip(survey, choices):
        if score == 4:
            continue

        if score < 4:
            result[question[0]] += 4 - score
        else:
            result[question[1]] += score % 4

    answer = ''

    if result['R'] >= result['T']:
        answer += 'R'
    else:
        answer += 'T'
    if result['C'] >= result['F']:
        answer += 'C'
    else:
        answer += 'F'
    if result['J'] >= result['M']:
        answer += 'J'
    else:
        answer += 'M'
    if result['A'] >= result['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer

while 1:
    try:
        print(solution(input().split()))
    except:
        break