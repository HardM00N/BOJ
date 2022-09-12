'''
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오. 

1. 길이가 짧은 것부터
2. 길이가 같으면 사전 순으로 
'''

words = []

for _ in range(int(input())):

    word = input()
    if (word, len(word)) in words:  # 단어가 이미 리스트에 있을 경우 추가하지 않음 (중복 제거)
        continue

    words.append((word, len(word))) # 단어와 단어의 길이를 리스트에 추가

words.sort(key = lambda x: (x[1], x[0]))    # 단어의 길이로 우선 정렬하고, 그 다음으로 단어로 정렬

for word in words:
    print(word[0])

'''
회고 / TIL
- 지난 알고리즘 스터디 때 공부한 정렬 파트에서 정렬 라이브러리의 key 파라미터를 이용했음. 
- key에 다중 조건을 설정할 수 있음을 이용해 풀었음. 
'''