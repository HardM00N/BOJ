# https://school.programmers.co.kr/learn/courses/30/lessons/42586

# 나의 풀이
def solution(progresses, speeds):    
    answer = []
    
    while progresses:
        cnt = 0
        
        while progresses and progresses[0] >= 100:      # 기능 개발이 완료되었다면
            cnt += 1
            progresses.pop(0)
            speeds.pop(0)
            
        progresses = [progresses[i] + speeds[i] for i in range(len(progresses))]
        
        if cnt:                                         # 완료된 작업이 있다면
            answer.append(cnt)
    
    return answer

'''
- zip 없는 무식한 풀이... 코테 감 잃은 거 티나는 풀이
- 다른 사람의 풀이는 워낙 다양해서 가져오지 않음. zip을 쓰자.
'''