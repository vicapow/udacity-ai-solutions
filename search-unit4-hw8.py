# ----------
# User Instructions:
# 
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

def search():
    # ----------------------------------------
    # insert code here and make sure it returns the appropriate result
    # ----------------------------------------
    path = []
    search_list = [[0, 0, 0]]
    
    while(len(search_list)):
        # check to see if we've arrived at our goal
        for item in search_list:
           if item[1] == goal[0] and item[2] == goal[1]:
               return item
        
        # find the next possible location with the smallest g value so far
        min_item = None
        for item in search_list:
            if(min_item is None):
                min_item = item
            elif(item[0] < min_item[0]):
                min_item = item
        
        # expand out to all adjacent blocks around min_item
        for d in delta:
            tmp = [ min_item[1] + d[0], min_item[2] + d[1] ]
            # if the possible pos is out of bounds, forget about it!
            if tmp[0] < 0 or tmp[0] >= len(grid) or tmp[1] < 0 or tmp[1] >= len(grid[0]):
                continue
            # if this location is blocked, forget about it!
            elif grid[tmp[0]][tmp[1]] == 1:
                continue
            else:
                # this new block is a possible block along our route
                search_list.append( [min_item[0] + 1, tmp[0], tmp[1] ])
        
        # we've expanded min_item so remove it from the list to prevent it from being expanded again
        search_list.remove(min_item)
        grid[min_item[1]][min_item[2]] = 1
    
    return "fail"

print search()