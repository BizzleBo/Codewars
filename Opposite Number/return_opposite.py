# Goal - 
# Very simple, given an integer or a 
# floating-point number, find its opposite.

# Given code - 
# def opposite(number):
  # your solution here

# Solution - 
def opposite(number):
    if number < 0:
        return float(abs(number))
    if number > 0:
        return float(-abs(number))
    else:
        return 0