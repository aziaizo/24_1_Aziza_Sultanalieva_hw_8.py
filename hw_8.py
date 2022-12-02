import sqlite3

def create_connection(db_file):
    conn=None
    try:
        conn=sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

create_products_table='''
create table products (
id integer primary key autoincrement,
product_title varchar(200) not null,
price double(10,2) not null default 0.0,
quantity integer(5) not null default 0
)
'''
def create_table(conn,sql):
    try:
        cursor=conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_product(conn,product):
    try:
        sql='''
        insert into products(product_title, price, quantity)
        values(?, ?, ?)
        '''
        cursor = conn.cursor()
        cursor.execute(sql,product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    return conn

def update_quantity(conn,product):
    try:
        sql = '''
          update products set quantity=? where id=?
           '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    return conn

def update_price(conn,product):
    try:
        sql = '''
          update products set price=? where id=?
           '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    return conn

def delete(conn,id):
    try:
        sql = '''
          delete from products where id=?
           '''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    return conn

def print_all_products(conn):
    try:
        sql = '''
        select * from products
           '''
        cursor = conn.cursor()
        cursor.execute(sql)
        r=cursor.fetchall()
        for row in r:
            print(row)
    except sqlite3.Error as e:
        print(e)
    return conn

def choose_products(conn):
    try:
        sql = '''
        select * from products where price<100 and quantity>5
           '''
        cursor = conn.cursor()
        cursor.execute(sql)
        r=cursor.fetchall()
        for row in r:
            print(row)
    except sqlite3.Error as e:
        print(e)
    return conn

def search_products(conn):
    try:
        sql = '''
        select * from products where lower(product_title) like '%smartphone%'
        '''
        cursor = conn.cursor()
        cursor.execute(sql)
        r=cursor.fetchall()
        for row in r:
            print(row)
    except sqlite3.Error as e:
        print(e)
    return conn


database=r'hw.db'
connect=create_connection(database)
if connect is not None:
    print('Connected')
    # create_table(connect,create_products_table)
    # create_product(connect,('Smartphone Xiaomi',59.9,2300))
    # create_product(connect, ('TV', 699, 1000))
    # create_product(connect, ('Computer', 1000, 150))
    # create_product(connect, ('Notebook', 477, 1500))
    # create_product(connect, ('Waschmaschine', 705.9, 150))
    # create_product(connect, ('Fridge', 90.5, 1100))
    # create_product(connect, ('Smartphone Samsung', 140.99, 300))
    # create_product(connect, ('Hoover', 230.86, 2000))
    # create_product(connect, ('Camera Sony', 89.45, 1220))
    # create_product(connect, ('Dishwasher', 459.99, 1890))
    # create_product(connect, ('Radio', 15.0, 100))
    # create_product(connect, ('Camera Hıkıvısıon', 337.49, 1234))
    # create_product(connect, ('Smartphone Apple', 100.9, 190))
    # create_product(connect, ('Headphones', 19.9, 2800))
    # create_product(connect, ('Watch', 89.6, 1650))
    # update_quantity(connect,(1234,4))
    # update_price(connect,(29.9,11))
    # delete(connect,11)
    # print_all_products(connect)
    # choose_products(connect)
    # search_products(connect)
    print('Done')