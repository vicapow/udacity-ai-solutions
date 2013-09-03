# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D() below.
#
# You are given a car in a grid with initial state
# init = [x-position, y-position, orientation]
# where x/y-position is its position in a given
# grid and orientation is 0-3 corresponding to 'up',
# 'left', 'down' or 'right'.
#
# Your task is to compute and return the car's optimal
# path to the position specified in `goal'; where
# the costs for each motion are as defined in `cost'.

# EXAMPLE INPUT:

# grid format:
#     0 = navigable space
#     1 = occupied space
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]
goal = [2, 0] # final position
init = [4, 3, 0] # first 2 elements are coordinates, third is direction
cost = [2, 1, 20] # the cost field has 3 values: right turn, no turn, left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D() should return the array
# 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
#
# ----------


# there are four motion directions: up/left/down/right
# increasing the index in this array corresponds to
# a left turn. Decreasing is is a right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right

forward_name = ['up', 'left', 'down', 'right']

# the cost field has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']


# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D():
  value = [[[999 for row in range(len(grid[0]))] for col in range(len(grid))],
          [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
          [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
          [[999 for row in range(len(grid[0]))] for col in range(len(grid))]]
  change = True
  while change:
    change = False
    for d in range(len(value)): # all orientations
      for x in range(len(value[d])):
        for y in range(len(value[d][x])): #all positions
          # check for goal
          if goal[0] is x and goal[1] is y:
            if value[d][x][y] > 0:
              value[d][x][y] = 0
              change = True
          # this grid space is navigable
          elif grid[x][y] is 0:
            for a in range(len(action)):
              d2 = (d + action[a]) % len(forward)
              f = forward[d2]
              x2 = x + f[0]
              y2 = y + f[1]
              # check if the grid pos is not navigable
              if x2 < 0 or x2 >= len(value[d2]): continue
              if y2 < 0 or y2 >= len(value[d2][x]): continue
              if grid[x2][y2] is not 0: continue
              v2 = value[d2][x2][y2] + cost[a]
              if v2 < value[d][x][y]:
                value[d][x][y] = v2
                change = True
  # trace the best policy
  policy = [ [' ' for row in range(len(grid[0]))] for col in range(len(grid)) ]
  home = False
  pos = [init[0], init[1], init[2]]
  while not home:
    cheapest = None
    cheapest_turn = None
    for a in range(len(action)):
      d2 = (pos[2] + action[a]) % len(forward)
      f = forward[d2]
      x2 = pos[0] + f[0]
      y2 = pos[1] + f[1]
      if x2 < 0 or x2 >= len(value[d2]): continue
      if y2 < 0 or y2 >= len(value[d2][x]): continue
      if grid[x2][y2] is not 0: continue
      if x2 is goal[0] and y2 is goal[1]:
        policy[x2][y2] = '*'
        home = True
      v2 = value[d2][x2][y2]
      if not cheapest or v2 + cost[a] < value[cheapest[2]][cheapest[0]][cheapest[1]] + cost[cheapest_turn]:
        cheapest = [x2, y2, d2]
        cheapest_turn = a
    if cheapest is None: home = True
    policy[pos[0]][pos[1]] = action_name[cheapest_turn]
    pos = cheapest


  return policy

policy = optimum_policy2D()

for row in policy:
  print row
