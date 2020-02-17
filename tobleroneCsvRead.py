import csv
from collections import defaultdict
#read csv and return a list
def readCsv(path):
    columns = defaultdict(list)
    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            for (i,v) in enumerate(row):
                columns[i].append(v)
    return columns            