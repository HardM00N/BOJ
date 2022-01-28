r, c, w = map(int, input().split())

pas = [[1], [1, 1]]
sum = 0

for i in range(2, r + w - 1):
    row = [1]
    for j in range(1, i):
        row.append(pas[i - 1][j - 1] + pas[i - 1][j])
    row.append(1)
    pas.append(row)
    
idx = 1

for i in range(r - 1, r + w - 1):
    for j in range(idx):
        sum += pas[i][c - 1 + j]
    idx += 1
print(sum)