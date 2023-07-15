import psycopg2
from psycopg2.extras import DictCursor


def connect():
    conn = psycopg2.connect("dbname=surfboard_db")
    cur = conn.cursor()
    return conn, cur


def close(conn, cur):
    cur.close()
    conn.close()


def create_tables(cur, sql_file):
    with open(sql_file, "r") as file:
        queries = file.read()
    cur.execute(queries)
    conn.commit()
    close(conn, cur)


conn, cur = connect()
create_tables(cur, "schema.sql")


def insert(cur, sql_file):
    with open(sql_file, "r") as file:
        # open function opens sql file in read mode ("r") and assigns it to the file variable, so we can call the read() method that reads the whole content of the file as a string and assigns to the queries variable. The with statement ensures the file is closed after reading.
        queries = file.read()
    cur.execute(queries)
    conn.commit()
    close(conn, cur)


conn, cur = connect()
insert(cur, "seed.sql")
