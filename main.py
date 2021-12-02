# solve sudoku(number place)

# backTracks = 0

# grid input from txt file
inputGrid = []
with open('input.txt', 'r') as f:
	for line in f:
		line = line.strip()
		line = line.replace('\n', '')
		line = line.split(",")
		inputGrid.append(line)

for j in range(len(inputGrid)):
	for i in range(len(line)):
		inputGrid[j][i] = int(inputGrid[j][i])
[print(i) for i in inputGrid]

def findNextCell(grid):
	for y in range(9):
		for x in range(9):
			if grid[y][x] == 0:
				return y, x
	return -1, -1

def isValid(grid, y, x, val):
	isRow = val not in grid[y]	# bool
	isCol = val not in [i[x] for i in grid]	# bool
	blk_x, blk_y = (x//3) * 3, (y//3) * 3	# 3 or 6 or 9
	blkGrid = [i[blk_x:blk_x + 3] for i in grid[blk_y:blk_y + 3]]	# 3x3grid
	isBlk = val not in sum(blkGrid, [])	# bool, sum to linearArray
	return all([isRow, isCol, isBlk])

def solveSudoku(grid, y=0, x=0):	# saiki
	global backTracks
	y, x = findNextCell(grid)
	if y == -1 or x == -1:
		return True
	for value in range(1, 10):
		if isValid(grid, y, x, value):
			grid[y][x] = value
			if solveSudoku(grid, y, x):	# saiki
				return True
			# backTracks += 1
			grid[y][x] = 0
	return False

print(solveSudoku(inputGrid))
# print(backTracks)
[print(i) for i in inputGrid]
