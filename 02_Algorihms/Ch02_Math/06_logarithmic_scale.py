import math

def log_scale(data, base):
    """
    Applies a logarithmic scale to a list of data using the specified base.
    """
    return [math.log(x, base) for x in data]
