# solve sudoku(number place)

# input sudoku-arr from other file
def fileInput(grid):
	with open('perterns.txt', 'r') as f:
		inputfile = f.readlines()

	# 改行文字を取り除く
	file = [line.strip() for line in inputfile]

	# 'select'の文字がある行を探す
	selectNum = [i for i, line in enumerate(file) if 'select' in line]

	# grid = []
	for num in selectNum:
		for line in file[num+1 : num+10]:
			line = line.replace('\n', '')
			line = line.split(',')
			grid.append(line)

	# int型に変換
	for j in range(len(grid)):
		for i in range(len(line)):
			grid[j][i] = int(grid[j][i])

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
			if solveSudoku(grid, y, x):
				return True
			backTracks += 1
			grid[y][x] = 0
	return False

grid = []
fileInput(grid)
print('<< input >>')
[print(i) for i in grid]

backTracks = 0

if solveSudoku(grid):
	print('\nSuccess!!\tloopback : ' + str(backTracks) + '\n')
else:
	print('\nfailed..\n')

print('<< output >>')
[print(i) for i in grid]
