import os

import psycopg2
import psycopg2.extras


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
                "port": os.environ.get("DB_PORT"),
            }
            print("Connecting to the postgreSQL database...")

            self.connection = psycopg2.connect(**self.param)
            self.cursor = self.connection.cursor()

            # Cursor for returning dict like values
            self.cursorx = self.connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            )

            print("PostgreSQL database version:")

            self.cursor.execute("SELECT version()")
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
        print("Database Connection Terminated!")

    def load_database(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS rapgen_database (
            id BIGSERIAL NOT NULL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            email VARCHAR(150) UNIQUE,
            gender VARCHAR(6) NOT NULL,
            date_of_birth DATE,
            phone_number VARCHAR(14) NOT NULL,
            role VARCHAR(12) NOT NULL DEFAULT 'visitor',
            region VARCHAR(100),
            joined date DEFAULT CURRENT_TIMESTAMP
        )
        """
        )
        self.connection.commit()
        print("Created Database!")

    @property
    def active(self):
        if self.connection:
            return "Connection is active!"
        return "Connection Failed!"

    @staticmethod
    def init_app():
        pass

    def add_data(self, data: dict):
        with self.connection:
            self.cursor.execute(
                """INSERT INTO rapgen_database(first_name, last_name, email, gender, date_of_birth, phone_number, role, region) 
            VALUES (%(first_name)s, %(last_name)s, %(email)s, %(gender)s, 
            %(date_of_birth)s, %(phone_number)s, %(role)s, %(region)s)
            """,
                data,
            )
        return self.get_last_column()

    def get_last_column(self):
        self.cursorx.execute("SELECT * FROM rapgen_database ORDER BY id DESC LIMIT 1;")
        return self.cursorx.fetchone()

    def user_exists(self, first_name: str, email: str):
        self.cursor.execute(
            """SELECT * FROM rapgen_database
        WHERE first_name=%(first_name)s AND email=%(email)s
        """,
            {"first_name": first_name, "email": email},
        )
        return self.cursor.fetchone()
