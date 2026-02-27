def get_estimated_spread(audiences_followers):
    """
    Calculates the estimated spread of a post using exponential growth.
    """
    if not audiences_followers:
        return 0

    avg = sum(audiences_followers) / len(audiences_followers)
    total_spread = avg * (len(audiences_followers) ** 1.2)
    
    return total_spread