number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][1]) #number_grid[row][col]

for row in number_grid:
    #print(row)
    for col in row:
        print(col)