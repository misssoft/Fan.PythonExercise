"""
Distribute a depth value into the right bin by binary search
"""

def binary_search_distribution(boundaries, depth, lower, upper):
    """
    :param boundaries: a list containing the boundary values of different bins in ascending order
    :param depth: the depth value of a pixel
    :param lower: position of lower boundaries
    :param upper: position of upper boundaries
    :return: the bin number
    """
    if lower + 1 == upper:
        return upper
    else:
        middle = (lower + upper) //2
        if depth > boundaries[middle]:
            return binary_search_distribution(boundaries, depth, middle, upper)
        else:
            return binary_search_distribution(boundaries, depth, lower, middle)
            
