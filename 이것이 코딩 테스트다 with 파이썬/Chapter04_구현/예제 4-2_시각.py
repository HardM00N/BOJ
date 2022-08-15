'''
정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서
3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오. 
예를 들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각이다. 

- 00시 00분 03초
- 00시 13분 30초

반면에 다음은 3이 하나도 포함되어 있지 않으므로 세면 안 되는 시각이다. 

- 00시 02분 55초
- 01시 27분 45초
'''

# 내 풀이
import time
start = time.time() # 시작

n = int(input())
cnt = 0

for h in range(0, n + 1):
    for m in range(60):    
        for s in range(60):
            
            if h % 10 == 3:
                cnt += 1
            elif m // 10 == 3:
                cnt += 1
            elif m % 10 == 3:
                cnt += 1
            elif s // 10 == 3:
                cnt += 1
            elif s % 10 == 3:
                cnt += 1

print(cnt)

end = time.time() - start   # 끝
print(end)

# 4-2.py 답안 예시
start = time.time() # 시작
h = int(input())

count = 0
for i in range(h + 1):
	for j in range(60):
		for k in range(60):
			# 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
				if '3' in str(i) + str(j) + str(k):
					count += 1

print(count)
end = time.time() - start   # 끝
print(end)
'''
회고 / TIL
- 내 풀이의 시간을 쟀을 때 2초를 초과하는 경우가 있어서 잘못 짠 줄 알았음. 
- 동빈님 코드도 동일하게 3중 반복문에, 2초를 초과하는 경우가 나오는데 대회에서 정확히 어떤 기준으로 초를 재는지 궁금함. 
- 내 로컬에서는 1초에서 3초 사이 왔다갔다 하는 것 같음. 
'''