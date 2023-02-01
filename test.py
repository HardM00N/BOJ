def solution(s):
    res = []
    
    while s:
        if len(s) < 2:
            res.append(s)
            break

        temp_x = s[0]
        temp_y = s[1]

        if temp_x != temp_y:
            res.append(s[:2])
            s = s[2:]
            continue
        
        else:
            cnt_x, cnt_others = 2, 0

            for i in s[2:]:
                if i == temp_x:
                    cnt_x += 1
                else:
                    cnt_others += 1

                if cnt_x == cnt_others:
                    res.append(s[:cnt_x + cnt_others])
                    s = s[cnt_x + cnt_others:]
                    break
            else:
                res.append(s)
                s = ''
        
    return len(res)

while 1:
    try:
        print(solution(input()))
    except:
        break