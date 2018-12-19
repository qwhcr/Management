import csv
import datetime
#
# def clean_newline(name):
#     data = []
#     temp = None
#     with open(name) as f:
#         for line in f:
#             if line.endswith('n\n'):
#                 if temp:
#                     line = temp + line
#                     temp = None
#                 data.append(line)
#             else:
#                 temp = line
#                 temp.replace('\n', '')
#     return data


def format_date(date_str):
    temp = str(date_str).split('/')
    temp[2] = '20' + temp[2]
    return datetime.date(int(temp[2]), int(temp[0]), int(temp[1]))


def read_from_source(name):
    data = []
    r = 0
    c = 0
    with open(name) as file:
        reader = csv.reader(file, delimiter=',')
        print('Reading data from csv file')
        start = False
        for row in reader:
            r += 1
            if row[0] == '1':
                start = True
            if start:
                if 'END' not in row:
                    if row[len(row)-1] != 'n':
                        c = len(row)-1
                        raise ValueError("new line char in elements, error in row:%d col:%d" % (r, c))
                    else:
                        data.append(row)
    return data
