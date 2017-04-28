"""
Read water depth from a csv file, which has one column of data. 
The module reads the file into array.
As a script, it prints out the number of records

Script Example:
    python depth_read.py depths.csv
    7500

"""

import sys
import csv
def read_water_depths(filename):
    """
    Read csv file into an array
    :param filename: path and name of the file
    :return: array of water depth
    """
    depths = []
    with open(filename, 'r') as csvf:
        rows = csv.reader(csvf, delimiter=',')
        next(rows)
        for row in rows:
            depths.append(float(row[0]))
        return depths

if __name__ == '__main__':
    RECORDS = read_water_depths(sys.argv[1])
    print(len(RECORDS))
    