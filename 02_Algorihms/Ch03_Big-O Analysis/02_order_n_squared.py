def does_name_exist(first_names, last_names, full_name):
    """
    Returns whether full_name exists in combination of first and last name in O(n) time.
    """
    for first_name in first_names:
        for last_name in last_names:
            target_name = ' '.join([first_name, last_name])
            if target_name == full_name:
                return True
    return False
