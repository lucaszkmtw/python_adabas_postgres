import os


ADABAS_DATABASE = {
    'jclassname': 'de.sag.jdbc.adabasd.ADriver',
    'url': f"jdbc:adabasd://{os.getenv('ADABAS_IP')}/RUPABK/",
    'driver_args': {
        'user': os.getenv('ADABAS_USER'),
        'password': os.getenv('ADABAS_PASSWORD'),
    },
    'jars': 'settings/adabasd.jar'
}

POSTGRES_DATABASE = {
    'database': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': 5432,
    'user': 'postgres'
}
