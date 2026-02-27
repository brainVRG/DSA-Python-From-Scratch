def get_follower_prediction(follower_count, influencer_type, num_months):
    """
    Calculates predicted follower count using a geometric progression based on influencer type.
    """
    exp_num = 2
    if influencer_type == "fitness":
        exp_num = 4
    elif influencer_type =="cosmetic":
        exp_num = 3

    return follower_count * (exp_num ** num_months)