def find_minimum(nums):
    """
    Finds the minimum value in a list of numbers using a linear scan.
    """
    if not nums:
        return None
    
    minimum = float("inf")

    for num in nums:
        if num < minimum:
            minimum = num

    return minimum