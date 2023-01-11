# https://www.acmicpc.net/problem/2467

N = int(input())
sol = list(map(int, input().split()))

min = int(1e10)
mins = []

for i in range(N - 1):
    start = i + 1
    end = N - 1
    
    while start <= end:
        mid = (start + end) // 2
        _sum = sol[i] + sol[mid]
        
        if abs(_sum) < min:
            min = abs(_sum)
            mins = [sol[i], sol[mid]]
        
        if _sum < 0:
            start = mid + 1
        else:
            end = mid - 1
            
print(*mins)