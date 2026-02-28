def binary_search(target, arr):
    """
    Returns True if target exists in the sorted array using O(log N) binary search.
    """
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        median = (low + high) // 2
        
        if arr[median] == target:
            return True
        elif arr[median] < target:  
            low = median + 1
        else:                       
            high = median - 1
            
    return False