# Goal - Clock shows h hours, m minutes 
# and s seconds after midnight.
# Your task is to write a function which 
# returns the time since midnight in 
# milliseconds.

# Given code - 
# def past(h, m, s):
    # Good Luck!

# Solution - 
def past(h, m, s):
    return int(((s * 1000) + (m * 60000) + (h * 3600000)))
