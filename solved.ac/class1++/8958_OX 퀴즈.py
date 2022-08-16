t = int(input())

for _ in range(t):
    score, _sum = 0, 0
    ox = input()
    
    for i in ox:
        if i == 'O':
            score += 1
            _sum += score
        else:
            score = 0
    print(_sum)