import psycopg2
import psycopg2.extras

import os


class ConnDB:
    """Creates connection to database using 'config.py' file and returns access to the class.
    NB: Use this class as a Context manager --> # with statement"""

    def __init__(self):
        self.connection = None

    def __enter__(self):
        try:
            self.param = {
                    "host": os.environ.get("DB_HOST"),
                    "database": os.environ.get("DB_NAME"),
                    "password": os.environ.get("DB_PASSWORD"),
                    "user": os.environ.get("DB_USER"),
                    "port": os.environ.get("DB_PORT")}
            # print(self.param)
            print("Connecting to the postgreSQL database...")

            self.connection = psycopg2.connect(**self.param)
            self.cursor = self.connection.cursor()

            # Cursor for returning dict like values
            self.cursorx = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

            print('PostgreSQL database version:')

            self.cursor.execute('SELECT version()')
            psql_version = self.cursor.fetchone()
            print(psql_version)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        else:
            self.load_database()
            return self
        return None

    def __exit__(self, exc_type, exc_val, traceback):
        # self.cursor.execute("ROLLBACK")
        # self.connection.commit()
        if self.connection:
            self.cursor.close()
            self.cursorx.close()
            self.connection.close()
        print('Database Connection Terminated!')

    def load_database(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS rapgen_database (
            id BIGSERIAL NOT NULL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            email VARCHAR(150) UNIQUE,
            role VARCHAR(150) NOT NULL,
            joined date DEFAULT CURRENT_TIMESTAMP
        )
        """)
        self.connection.commit()
        print("Created Database!")

    @property
    def active(self):
        if self.connection:
            return 'Connection is active!'
        return 'Connection Failed!'

    @staticmethod
    def init_app():
        pass
