ADJ = 4

grid = []

with open('input_11', 'r') as f:

    for line in f.readlines():
        grid.append((line.strip()).split(' '))

mx = 0

for i in range(0, len(grid) - ADJ + 1):
    for j in range(0, len(grid) - ADJ + 1):
        pr = [1, 1, 1, 1, 1, 1, 1, 1]
        for k in range(0, ADJ):
            pr[0] *= int(grid[i][j+k])
            pr[1] *= int(grid[i][j-k])
            pr[2] *= int(grid[i+k][j])
            pr[3] *= int(grid[i-k][j])
            pr[4] *= int(grid[i+k][j+k])
            pr[5] *= int(grid[i-k][j-k])
            pr[6] *= int(grid[i-k][j+k])
            pr[7] *= int(grid[i+k][j-k])
        for p in pr:
            if p > mx:
                mx = p

print mx
