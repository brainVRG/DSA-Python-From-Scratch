def count_names(list_of_lists, target_name):
    """
    Counts the occurrences of a target name in a nested list in O(m*n) time.
    """
    count = 0
    
    for sublist in list_of_lists:
        for name in sublist:  
            if name == target_name:
                count += 1
                
    return count