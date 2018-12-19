import os.path
import View.ParserWrapper

if __name__ == '__main__':
    filename = os.path.dirname(__file__) + '/../file/11-水泥.csv'
    data = View.ParserWrapper.read_from_source(filename)
    db_manager = View.DBManager.DatabaseManager()
    db_manager.create()
    customer_set = set()
    for i in data:
        customer_set.add(i[5])

    db_manager.execute('SELECT * FROM CUSTOMERS')
    existing_customer = db_manager.fetch_all()

    for customer in customer_set:
        if customer not in existing_customer:
            command = "INSERT INTO CUSTOMERS VALUES('" + customer + "')"
            db_manager.execute(command)
    db_manager.commit()
    print(data[0])
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

