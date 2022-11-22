n = int(input())

coin = 0

while n > 0:
    if n % 5 == 0:
        coin += n // 5
        break
    n -= 2
    coin += 1
    
if n < 0:
    print(-1)
else:
    print(coin)
