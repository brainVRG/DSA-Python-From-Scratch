def num_possible_orders(num_posts):
    """
    Calculates the total possible orders (factorial) for a given number of posts.
    """
    answer = 1
    for num in range(1, num_posts+1):
        answer *= num
    return answer
