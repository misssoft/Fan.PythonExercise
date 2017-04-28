"""
Compute risk values of an area with water depth in a csv file
Two lists are based on the given vulnerability curve.BaseException
The first contains the boundaries of bins.
The second contains values of damage in different situations

Script example:
    python risk_estimation.py depths.csv
    [81272.25]
"""

import sys
import numpy as np
from binary_search_distribution import binary_search_distribution
from depth_read import read_water_depths


def main(filename):
    """
    Calcuate the risk value based on csv file of water depth
    :param filename: csv file name
    :return: expected damage value
    """
    boun = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    values = [0, 50000, 80000, 95000, 105000, 112500, 120000, 125000, 130000, 132500, 134000]
    probabilities = np.zeros((1, 11), dtype=np.float)
    depths = read_water_depths(filename)
    num_p = len(depths)
    total_p = int(num_p/0.75) #total number of pixels in the area

    for i in range(0, num_p):
        upper = binary_search_distribution(boun, depths[i], 0, len(boun))
        probabilities[0, upper] += 1.0
    probabilities /= total_p
    risk = np.dot(probabilities, values)
    print(risk)

if __name__ == '__main__':
    main(sys.argv[1])
