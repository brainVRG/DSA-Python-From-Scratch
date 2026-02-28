def find_last_name(names_dict, first_name):
    """
    Returns names dict contains value of first name key in constant O(1) time.
    """
    return names_dict.get(first_name, None)