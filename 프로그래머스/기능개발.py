def solution(progresses, speeds):    
    answer = []    
    
    while progresses :         
        fin = 0        
        
        while progresses and progresses[0] >= 100:
            fin += 1
            progresses.pop(0)
            speeds.pop(0)            
        
        progresses = [progresses[i] + speeds[i] for i in range(len(progresses))]    # 작업 진행        
        
        if fin:
            answer.append(fin)    
    
    return answer