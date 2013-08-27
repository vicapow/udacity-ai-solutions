# ----------
# User Instructions:
# 
# Create a function compute_value() which returns
# a grid of values. Value is defined as the minimum
# number of moves required to get from a cell to the
# goal. 
#
# If it is impossible to reach the goal from a cell
# you should assign that cell a value of 99.

# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

# for whatever reason, the grading submission system likes the grid to be in 
# the second format, not the first.

grid = [[0, 1, 0],
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost_step = 1 # the cost associated with moving from a cell to an adjacent one.

# ----------------------------------------
# insert code below
# ----------------------------------------

def compute_value():
    values = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    open = []
    open.append([0, goal[0], goal[1]])
    while len(open) > 0:
      open.sort()
      open.reverse()
      next = open.pop()
      v = next[0]
      x = next[1]
      y = next[2]
      values[x][y] = v
      for i in delta:
        x2 = x + i[0]
        y2 = y + i[1]
        if x2 >=0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and values[x2][y2] == -1:
          if(values[x2][y2] == -1 and grid[x2][y2] == 1):
            values[x2][y2] = 99
          else:
            open.append([v + 1, x2, y2])
    for i in range(len(values)):
      for j in range(len(values[0])):
        if values[i][j] == -1:
          values[i][j] = 99
    return values #make sure your function returns a grid of values as demonstrated in the previous video.

values = compute_value()
for i in values:
    print i