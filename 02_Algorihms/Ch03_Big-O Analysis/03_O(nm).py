def get_avg_brand_followers(all_handles, brand_name):
    """
    Returns average brand followers per influencer in O(n*m) time.
    """
    count = 0
    total_influencers = 0 

    for influencer_audience in all_handles:
        for handle in influencer_audience:
            if brand_name in handle:
                count += 1
        total_influencers += 1

    return count / total_influencers