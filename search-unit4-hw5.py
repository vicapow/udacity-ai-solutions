# --------------
# USER INSTRUCTIONS
#
# Write a function called stochastic_value that 
# takes no input and RETURNS two grids. The
# first grid, value, should contain the computed
# value of each cell as shown in the video. The
# second grid, policy, should contain the optimum
# policy for each cell.
#
# Stay tuned for a homework help video! This should
# be available by Thursday and will be visible
# in the course content tab.
#
# Good luck! Keep learning!
#
# --------------
# GRADING NOTES
#
# We will be calling your stochastic_value function
# with several different grids and different values
# of success_prob, collision_cost, and cost_step.
# In order to be marked correct, your function must
# RETURN (it does not have to print) two grids,
# value and policy.
#
# When grading your value grid, we will compare the
# value of each cell with the true value according
# to this model. If your answer for each cell
# is sufficiently close to the correct answer
# (within 0.001), you will be marked as correct.
#
# NOTE: Please do not modify the values of grid,
# success_prob, collision_cost, or cost_step inside
# your function. Doing so could result in your
# submission being inappropriately marked as incorrect.

# -------------
# GLOBAL VARIABLES
#
# You may modify these variables for testing
# purposes, but you should only modify them here.
# Do NOT modify them inside your stochastic_value
# function.

grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]]

goal = [0, len(grid[0])-1] # Goal is in top right corner


delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>'] # Use these when creating your policy grid.

success_prob = 0.5
failure_prob = (1.0 - success_prob)/2.0 # Probability(stepping left) = prob(stepping right) = failure_prob
collision_cost = 1000
cost_step = 1

############## INSERT/MODIFY YOUR CODE BELOW ##################
#
# You may modify the code below if you want, but remember that
# your function must...
#
# 1) ...be called stochastic_value().
# 2) ...NOT take any arguments.
# 3) ...return two grids: FIRST value and THEN policy.


def stochastic_value():
    def off_grid(x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[x]): return True
        return False
    value = [[collision_cost for row in range(len(grid[0]))] for col in range(len(grid))]
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    
    changed = True
    while changed:
        changed = False
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if x is goal[0] and y is goal[1]:
                    value[x][y] = 0
                    policy[x][y] = '*'
                    continue
                if grid[x][y] is 1: continue
                # examine adjacent cells
                for d_index in range(len(delta)):
                    d = delta[d_index] # direction we're thinking about trying to go
                    x2 = x + d[0]
                    y2 = y + d[1]
                    if off_grid(x2, y2): continue
                    # calculate cost_left
                    dleft = delta[(d_index + 1) % len(delta)]
                    x_left = x + dleft[0]
                    y_left = y + dleft[1]
                    if off_grid(x_left, y_left): cost_left = collision_cost
                    else: cost_left = value[x_left][y_left]
                    # calculate cost_right
                    dright = delta[(d_index - 1) % len(delta)]
                    x_right = x + dright[0]
                    y_right = y + dright[1]
                    if off_grid(x_right, y_right): cost_right = collision_cost
                    else: cost_right = value[x_right][y_right]
                    v2 = value[x2][y2] * success_prob + failure_prob * cost_left + failure_prob * cost_right + cost_step
                    if v2 < value[x][y]:
                        value[x][y] = v2
                        policy[x][y] = delta_name[d_index]
                        changed = True
    return value, policy

value, policy = stochastic_value()

print "value"
for row in value:
    print row

print "policy"
for row in policy:
    print row