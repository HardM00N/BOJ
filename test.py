S = input()
S_list = []

for i in range(len(S)):
    S_list.append(S[i:])

for s in sorted(S_list):
    print(s)