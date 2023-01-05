import pymysql

DROP_TABLE_USERS = "DROP TABLE IF EXISTS users"

USERS_TABLE = """CREATE TABLE users(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)"""

if __name__ == '__main__':
    try:
        connect = pymysql.Connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='sm-pass',
            db='pythondb',
        ) 
        cursor = connect.cursor()
        cursor.execute(DROP_TABLE_USERS)
        cursor.execute(USERS_TABLE)
        print('Conexión realizada de forma exitosa!')
    except pymysql.err.OperationalError as err:
        print('No fué posible realizar la conexión')
        print(err)