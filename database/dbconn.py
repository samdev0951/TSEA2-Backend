from typing import Generator

import MySQLdb
from MySQLdb.cursors import Cursor, DictCursor

import config as config

db_config = {
    "host": config.DB_HOST,
    "user": config.DB_USER,
    "password": config.DB_PASSWORD,
    "db": config.DB_NAME,
    "cursorclass": DictCursor
}

conn = MySQLdb.connect(**db_config) # Create a connection to the database
conn.autocommit(True)

# Gets the database cursor if valid
def get_cursor() -> Generator[Cursor, None, None]:
    cursor = conn.cursor()
    try:
        yield cursor
    finally:
        cursor.close()