n, k = map(int, input().split())

pas = [[1], [1, 1]]
for i in range(2, n):
    row = [1]
    for j in range(1, i):
        row.append(pas[i - 1][j - 1] + pas[i - 1][j])
    row.append(1)
    pas.append(row)

print(pas[n - 1][k - 1])