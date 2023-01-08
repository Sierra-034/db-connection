import pymysql
from decouple import config

DROP_TABLE_USERS = "DROP TABLE IF EXISTS users"

USERS_TABLE = """CREATE TABLE users(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)"""

users = [
    ('user1', 'password', 'user1@gmail.com'),
    ('user2', 'password', 'user2@gmail.com'),
    ('user3', 'password', 'user3@gmail.com'),
    ('user4', 'password', 'user4@gmail.com'),
    ('user5', 'password', 'user5@gmail.com'),
]

if __name__ == '__main__':
    try:
        connect = pymysql.Connect(
            host='127.0.0.1',
            port=3306,
            user=config('USER_MYSQL'),
            passwd=config('PASSWORD_MYSQL'),
            db=config('DB_MYSQL'),
        ) 
        with connect.cursor() as cursor:
            cursor.execute(DROP_TABLE_USERS)
            cursor.execute(USERS_TABLE)

            query = "INSERT INTO users(username, password, email) VALUES(%s, %s, %s)"
            cursor.executemany(query, users)
            connect.commit()

            query = "SELECT id, username, email FROM users WHERE id >= 3"
            rows = cursor.execute(query)
            for row in cursor.fetchall():
                print(row)

        print('Conexión realizada de forma exitosa!')
    except pymysql.err.OperationalError as err:
        print('No fué posible realizar la conexión')
        print(err)
    finally:
        print('finally exec')   # Finally siempre se ejecuta
        connect.close() # Esto también
