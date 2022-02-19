# Goal - 
# Given an array of integers, find the 
# one that appears an odd number of times.


# Given code -
# def find_it(seq):
#   return None

# Solution - 
def find_it(seq):
    return min([n for n in seq if seq.count(n) % 2 != 0]) 