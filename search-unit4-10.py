# -----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
# 
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left, 
# up, and down motions. NOTE: the 'v' should be 
# lowercase.
#
# Your function should be able to do this for any
# provided grid, not just the sample grid below.
# ----------


# Sample Test case
grid = [[0, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

# ----------------------------------------
# modify code below
# ----------------------------------------

def printGrid(grid):
    for i in range(len(grid)):
        print grid[i]

def search():
    delta_name = ['v', '>', '^', '<']
    expand = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    vals = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1

    x = init[0]
    y = init[1]
    g = 0
    vals[0][0] = 0
    open = [[g, x, y]]

    found = False  # flag that is set when search is complet
    resign = False # flag set if we can't find expand

    while not found and not resign:
        if len(open) == 0:
            resign = True
            return 'fail'
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]
            
            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            vals[x2][y2] = g2
                            closed[x2][y2] = 1
    pos = [goal[0], goal[1]]
    expand[goal[0]][goal[1]] = '*'
    path_len = vals[pos[0]][pos[1]]
    for i in range( vals[ goal[0] ] [ goal[1] ] ):
        for index, d in enumerate(delta):
            tmp = [ pos[0] + d[0], pos[1] + d[1] ]
            if tmp[0] < 0 or tmp[0] >= len(grid) or tmp[1] < 0 or tmp[1] >= len(grid[0]):
                continue
            elif vals[tmp[0]][tmp[1]] is path_len - 1:
                expand[tmp[0]][tmp[1]] = delta_name[index]
                path_len = path_len - 1
                pos = tmp
                break
        else:
            continue
    return expand


expand = search()
printGrid(expand)