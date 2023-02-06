def GCD(a, b):
    if a < b:
        a, b = b, a
    
    while b:
        a, b = b, a % b

    return a

while 1:
    try:
        N = int(input())
        rings = list(map(int, input().split()))
        
        for i in range(1, N):
            gcd = GCD(rings[0], rings[i])
            print('{}/{}'.format(rings[0] // gcd, rings[i] // gcd))

    except:
        break