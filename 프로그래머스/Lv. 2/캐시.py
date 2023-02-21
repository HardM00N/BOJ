# https://school.programmers.co.kr/learn/courses/30/lessons/17680

# 나의 풀이
def solution(cacheSize, cities):
    if not cacheSize:                       # 캐시 사이즈가 0이면 모두 캐시 미스이므로
        return len(cities) * 5              # cities의 길이 * 5 리턴

    time = 0                                # 시간
    cache = {}                              # 캐시 딕셔너리
    
    for city in cities:                     # cities를 돌면서
        city = city.lower()                 # city는 모두 소문자 처리

        for i in cache:                     # 캐시 내의 모든 city들의 나이를 1 증가
            cache[i] += 1

        if len(cache) < cacheSize:          # 아직 캐시에 여유 공간이 있다면 캐시에 적재를 하되,
            if city in cache:               # city가 이미 캐시에 있다면
                cache[city] = 0             # 해당 city의 나이를 0으로 초기화
                time += 1                   # 캐시 적중 시간
            else:                           # city가 캐시에 없었다면
                cache[city] = 0             # 해당 city를 캐시에 신규 적재
                time += 5                   # 캐시 미스 시간
        
        else:                               # 캐시가 꽉 찼는데
            if city in cache:               # 캐시 적중이라면
                cache[city] = 0             # 해당 city 나이 초기화
                time += 1                   # 캐시 적중 시간
            else:                           # 캐시 미스라면
                del cache[max(cache.keys(), key=lambda x: cache[x])]    # 나이가 가장 많은 city 캐시에서 제거
                cache[city] = 0                                         # 신규 city 캐시에 적재
                time += 5                                               # 캐시 미스 시간

    return time

# 다른 사람의 풀이
def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)                         # 캐시 사이즈 제한
    
    time = 0
    
    for i in cities:
        s = i.lower()
        
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)                                             # 어차피 maxlen 때문에 알아서 삭제됨.
            time += 5
    
    return time

'''
회고 / TIL
- 졸업하고 오랜만에 듣는 LRU... 어쨌든 캐시가 꽉 찼다면 가장 오래된 녀석을 삭제하는 기법임.
- 딕셔너리로 key에 도시, value에 캐시에 적재된 이후로 먹은 나이를 넣어서 계산했음.
- 다른 사람의 풀이는 큐를 활용함. 큐에서 오래된 녀석을 삭제하고 다시 넣기가 귀찮어서 딕셔너리로 풀었는데, maxlen을 쓰니 큐도 nice함.
'''