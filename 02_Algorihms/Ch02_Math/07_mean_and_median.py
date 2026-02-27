def average_followers(nums):
    """
    Calculates the average (mean) of a list of numbers.
    """
    if not nums:
        return None

    total = 0
    length = 0
    
    for num in nums:
        total += num
        length += 1

    return total / length
