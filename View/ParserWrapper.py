import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import csv
import datetime
from View import DBManager
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
def read_from_file(filename):
    filename = filename
    data = read_from_source(filename)
    db_manager = DBManager.DatabaseManager()
    db_manager.create()
    customer_set = set()
    for i in data:
        customer_set.add(i[5])

    for i in data:
        if i[6] == '':
            i[6] = '无'
        date = i[1].split('/')
        command = f'''INSERT INTO ORDERS VALUES (
        20{date[2]}, 
        {date[0]},
        {date[1]},
        '{i[2]}',
        '{i[3]}',
        '{i[5]}',
        {float(i[4])},
        0.0,
        '{i[6]}',
        0)
        '''
        db_manager.execute(command)
    db_manager.commit()
    db_manager.close()

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
