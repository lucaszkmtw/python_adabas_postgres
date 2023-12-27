import jaydebeapi
import psycopg2
from settings.config import ADABAS_DATABASE
from settings.config import POSTGRES_DATABASE


class AdabasConnection(object):
    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection = jaydebeapi.connect(**ADABAS_DATABASE)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()


class PostgresConnection(object):
    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection = psycopg2.connect(**POSTGRES_DATABASE)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()


if __name__ == '__main__':
    with PostgresConnection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """"""
            )
