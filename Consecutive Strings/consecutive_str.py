# Goal - 
# You are given an array(list) strarr of 
# strings and an integer k. Your task is to
# return the first longest string 
# consisting of k consecutive strings 
# taken in the array.

# Given -
# def longest_consec(strarr, k):
    # your code

# Solution - 
def longest_consec(strarr, k):
    result = ""

    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index+k])
            if len(s) > len(result):
                result = s

    return result