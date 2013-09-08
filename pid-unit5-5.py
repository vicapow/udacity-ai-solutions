# -----------
# User Instructions
#
# Define a function smooth that takes a path as its input
# (with optional parameters for weight_data, weight_smooth)
# and returns a smooth path.
#
# Smoothing should be implemented by iteratively updating
# each entry in newpath until some desired level of accuracy
# is reached. The update should be done according to the
# gradient descent equations given in the previous video:
#
# If your function isn't submitting it is possible that the
# runtime is too long. Try sacrificing accuracy for speed.
# -----------


from math import *

# Don't modify path inside your function.
path = [[0, 0],
        [0, 1],
        [0, 2],
        [1, 2],
        [2, 2],
        [3, 2],
        [4, 2],
        [4, 3],
        [4, 4]]

# ------------------------------------------------
# smooth coordinates
#

def smooth(path, weight_data = 0.5, weight_smooth = 0.1, tolerance = 0.000001 ):

    newpath = [[0 for col in range(len(path[0]))] for row in range(len(path))]
    #### ENTER CODE BELOW THIS LINE ###
    def vec_add(vec1, vec2):
        return [vec1[0] + vec2[0], vec1[1] + vec2[1]]
    
    def vec_minus(vec1, vec2):
        return [vec1[0] - vec2[0], vec1[1] - vec2[1]]

    def vec_scale(vec, s):
        return [vec[0] * s, vec[1] * s]
    def dist(vec1, vec2): # euclidean distance
        dx = vec2[0] - vec1[0]
        dy = vec2[1] - vec1[1]
        return sqrt( dx * dx + dy * dy )

    # Make a deep copy of path into newpath
    for i in range(len(path)): newpath[i] = vec_add(path[i], [0, 0])
    change = tolerance
    while change >= tolerance:
        change = 0.0
        for i in range(len(path)):
            # skip the first and last points
            before = vec_add(newpath[i], [0, 0]) #copy
            if i is 0 or i is len(newpath) - 1: continue
            # apply alpha (weight_data)
            newpath[i] = vec_add(
                newpath[i], 
                vec_scale( 
                    vec_minus(path[i], newpath[i]), 
                    weight_data 
                )
            )
            # apply beta (weighted_smooth)
            newpath[i] = vec_add(
                newpath[i], 
                vec_scale( 
                    vec_minus( 
                        vec_add( newpath[i + 1] , newpath[i - 1] ), 
                        vec_scale( newpath[i], 2)
                    ), 
                    weight_smooth
                )
            )
            change += dist(before, newpath[i])
    return newpath # Leave this line for the grader!

# feel free to leave this and the following lines if you want to print.
newpath = smooth(path)

# thank you - EnTerr - for posting this on our discussion forum
for i in range(len(path)):
    print '['+ ', '.join('%.3f'%x for x in path[i]) +'] -> ['+ ', '.join('%.3f'%x for x in newpath[i]) +']'
