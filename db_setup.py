import psycopg2
from psycopg2.extras import DictCursor
import bcrypt

def connect():
    # conn = psycopg2.connect("dbname=surfboard_db")
    conn = psycopg2.connect(
    host='dpg-cintu85gkuvudi85lii0-a',
    port=5432,
    dbname='surfboard_project',
    user='surfboard_project_user',
    password='Kl4A5PcUULa4dyy1FrnOBwygs1PFb8Xm',
)
    cur = conn.cursor(cursor_factory=DictCursor)
    return conn, cur


def close(conn, cur):
    cur.close()
    conn.close()

def drop_tables():
    conn, cur = connect()
    cur.execute("DROP TABLE surfboards")
    conn.commit()
    
    cur.execute("DROP TABLE shapers")
    conn.commit()
    
    cur.execute("DROP TABLE stores")
    conn.commit()

def create_tables(sql_file):
    with open(sql_file, "r") as file:
        queries = file.read()
        cur.execute(queries)
        conn.commit()


password = "test"
binary_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
password_hash = binary_password.decode()

def insert_password(password_hash):
    conn, cur = connect()
    cur.execute(
    "INSERT INTO shapers (id, shaper_name, email, shaper_url, is_admin, password_hash) VALUES (%s, %s, %s, %s, %s, %s)",
    (
        1,
        'JS Industries',
        'jsindustries@email.com',
        'https://jsindustries.com/',
        True,
        password_hash
    )
        )
    conn.commit()
    
    cur.execute(
        "INSERT INTO shapers (id, shaper_name, email, shaper_url, is_admin, password_hash) VALUES (%s, %s, %s, %s, %s, %s)",
    (
        2,
        'Channel Island',
        'allmerick@email.com',
        'https://shop-au.cisurfboards.com/',
        True,
        password_hash
    )
        )
    conn.commit()

    cur.execute(
        "INSERT INTO shapers (id, shaper_name, email, shaper_url, is_admin, password_hash) VALUES (%s, %s, %s, %s, %s, %s)",
        (
        3,
        'Pyzel Surfboards',
        'pyzel@email.com',
        'https://pyzelsurf.com.au/',
        True,
        password_hash
    )
        )
    conn.commit()
    close(conn, cur)


def insert(sql_file):
    with open(sql_file, "r") as file:
        # open function opens sql file in read mode ("r") and assigns it to the file variable, so we can call the read() method that reads the whole content of the file as a string and assigns to the queries variable. The with statement ensures the file is closed after reading.
        
        queries = file.read()
        cur.execute(queries)
        conn.commit()

if __name__ == "__main__":
        conn, cur = connect()
        drop_tables()
        create_tables("schema.sql")
        insert_password(password_hash)
        insert("seed.sql")
        close(conn, cur)