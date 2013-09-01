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
           [ 0,  1]] # do right
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
    for d in range(len(value)):
      for x in range(len(value[d])):
        for y in range(len(value[d][x])):
          # check for goal
          if goal[0] is x and goal[1] is y:
            if value[d][x][y] > 0:
              value[d][x][y] = 0
              change = True
          # this grid space is navigable
          elif grid[x][y] is 0:
            # iterate over the pos/orientations that could move here
            for a in action:
              # when we go backwards in time, a right turn because a left turn
              prev_d = (d - a) % len(forward)
              f = forward[prev_d]
              x2 = x - f[0]
              y2 = x - f[1]
              if x2 < 0 or x2 >= len(value[d]) or y2 < 0 or y2 >= len(value[d][x]) or grid[x2][y2] is not 0: 
                continue
              v2 = value[d][x][y] + cost[a]
              print "v2", v2
              if value[prev_d][x2][y2] > v2:
                value[prev_d][x2][y2] = v2
                change = True
  
  # TODO: fix value (all values 999 expect goal)
  for orient in range(len(value)):
    print "orient:", orient
    for o in value[orient]:
      print o
  
  policy2D = [ [' ' for row in range(len(grid[0]))] for col in range(len(grid)) ]
  return policy2D # Make sure your function returns the expected grid.


optimum_policy2D()
