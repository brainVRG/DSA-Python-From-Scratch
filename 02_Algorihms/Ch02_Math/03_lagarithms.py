import math

def get_influencer_score(num_followers, average_engagement_percentage):
    """
    Calculate influencer's score by using a logarithmic formula
    """
    return average_engagement_percentage * math.log(num_followers, 2)
