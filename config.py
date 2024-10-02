import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'd64d153db414bf9e78089bd25a1c3eae8f4a765c4e')
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'Mayson@0902')
    MYSQL_DB = os.getenv('MYSQL_DB', 'africa_innovation_connect')

