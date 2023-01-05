import pymysql

if __name__ == '__main__':
    try:
        connnect = pymysql.Connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='sm-pass',
            db='pythondb',
        ) 

        print('Conexión realizada de forma exitosa!')
    except pymysql.err.OperationalError as err:
        print('No fué posible realizar la conexión')
        print(err)
