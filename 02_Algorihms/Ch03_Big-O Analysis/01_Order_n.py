def find_max(nums):
    """
    Returns the maximum number in a list in O(n) time.
    """
    if not nums:
        return None 
        
    max_val = -float("inf") 
    for num in nums:
        if num > max_val:
            max_val = num
            
    return max_val