import csv

def read_from_source(name):
    data = []
    with open(name) as file:
        reader = csv.reader(file, delimiter=',')
        line = 0
        print('Reading data from csv file')
        start = False
        for row in reader:
            if row[0] == '1':
                start = True
            if start:
                if 'END' not in row:
                    data.append(row)
    return data
