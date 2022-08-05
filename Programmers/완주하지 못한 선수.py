def solution(participant, completion):
    answer = ''
    for i in participant:
        if i == len(participant) - 1:
            answer = participant[i]
            break
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    return answer