def decayed_followers(initial_followers, fraction_lost_daily, days):
    """
    Calculates the remaining followers using an exponential decay formula.
    """
    return int(initial_followers * (1 - fraction_lost_daily) ** days)