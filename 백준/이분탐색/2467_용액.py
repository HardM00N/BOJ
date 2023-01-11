# https://www.acmicpc.net/problem/2467

N = int(input())
sol = list(map(int, input().split()))

res = int(1e9)
min_left, min_right = 0, 0

for i in range(N - 1):
    start = i + 1
    end = N - 1
    
    while start <= end:
        mid = (start + end) // 2
        _sum = sol[i] + sol[mid]
        
        if abs(_sum) < res:
            res = abs(_sum)
            min_left = i
            min_right = mid

            if _sum == 0:
                break
        
        if _sum < 0:
            start = mid + 1
        else:
            end = mid - 1
            
print(sol[min_left], sol[min_right])