while 1:
    try:
        N = input()
        if sum(list(map(int, N))) % 3 == 0 and '0' in N:
            print(''.join(sorted(list(N), reverse=True)))
            # print(sorted(list(N), reverse=True))
        else:
            print(-1)
    except:
        break