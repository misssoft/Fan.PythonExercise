"""
Read water depth from a csv file, which has one column of data
"""
import csv
def readcsvf(fileName):
    """
    Read csv file into an array
    :param fileName: path and name of the file
    :return: array of water depth
    """
    depths=[]
    with open(fileName,'r') as csvf:
        rows = csv.reader(csvf, delimiter = ',')
        header = next(rows)       
        for row in rows:
            depths.append(float(row[0]))
        return depths
    


    
