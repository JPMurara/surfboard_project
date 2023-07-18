import psycopg2
from psycopg2.extras import DictCursor


def connect():
    conn = psycopg2.connect("dbname=surfboard_db")
    cur = conn.cursor(cursor_factory=DictCursor)
    return conn, cur


def close(conn, cur):
    cur.close()
    conn.close()


def create_tables(sql_file):
    with open(sql_file, "r") as file:
        queries = file.read()
        cur.execute(queries)
        conn.commit()


def insert(sql_file):
    with open(sql_file, "r") as file:
        # open function opens sql file in read mode ("r") and assigns it to the file variable, so we can call the read() method that reads the whole content of the file as a string and assigns to the queries variable. The with statement ensures the file is closed after reading.
        queries = file.read()
        cur.execute(queries)
        conn.commit()


def insert_shaper(shaper_name, email, url, stored_password):
    conn, cur = connect()
    query = "INSERT INTO shapers (shaper_name, email, url, password_hash) VALUES (%s, %s, %s, %s)"
    data = (shaper_name, email, url, stored_password)
    cur.execute(query, data)
    conn.commit()
    close(conn, cur)


if __name__ == "__main__":
    # executes these func only when we can call the file directly: python3 model.py. Not when its imported as a module
    conn, cur = connect()
    create_tables("schema.sql")
    insert("seed.sql")
    close(conn, cur)
