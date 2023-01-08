from decouple import config

db_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': config('USER_MYSQL'),
    'passwd': config('PASSWORD_MYSQL'),
    'db': config('DB_MYSQL'),
}