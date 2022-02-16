def positive_sum(arr):
    # Your code here
    sum = 0
    for x in arr:
        if x > 0:
            sum = sum + x
    return sum