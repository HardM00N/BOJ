'''
ACM 호텔 매니저 지우는 손님이 도착하는 대로 빈 방을 배정하고 있다. 
고객 설문조사에 따르면 손님들은 호텔 정문으로부터 걸어서 가장 짧은 거리에 있는 방을 선호한다고 한다. 

-- 이하 문제가 길어서 생략함 --
https://www.acmicpc.net/problem/10250 참고
'''

T = int(input())

for _ in range(T):                          # test case 입력 받기
    H, W, N = map(int, input().split())
    cnt = 0

    for w in range(W):                      # 각 width마다 
        for h in range(H):                  # height를 우선적으로 순회하며
            cnt += 1                        # count함. 

            if cnt == N:                    # N번째 방에 도달하면 방 번호 출력
                print("%d%02d" % (h + 1, w + 1))
                break

'''
회고 / TIL
- 문제 의도만 파악하면 굉장히 쉬운 문제임. 
- 단순히 w를 고정한 채 h부터 높이면서 방을 채워나가면 됨. 
- 오히려 서식문자 사용이 더 어려웠던 것 같다. (봐도 봐도 제대로 기억이 안 남...)
'''