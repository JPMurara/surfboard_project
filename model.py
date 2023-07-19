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


def insert_shaper(shaper_name, email, shaper_url, stored_password):
    conn, cur = connect()
    cur.execute(
        "INSERT INTO shapers (shaper_name, email, shaper_url, password_hash) VALUES (%s, %s, %s, %s)",
        [shaper_name, email, shaper_url, stored_password],
    )
    conn.commit()
    close(conn, cur)


def search(min_wave_size, max_wave_size, wave_type, break_type, skill_level):
    conn, cur = connect()
    cur.execute(
        "SELECT * FROM surfboards LEFT JOIN shapers ON surfboards.shaper_id = shapers.id WHERE min_wave_size<=%s OR max_wave_size>=%s AND wave_type=%s AND break_type=%s AND skill_level=%s",
        [min_wave_size, max_wave_size, wave_type, break_type, skill_level],
    )
    exact_match = cur.fetchall()

    close(conn, cur)
    return exact_match


def get_user(email):
    conn, cur = connect()
    cur.execute(
        "SELECT * FROM shapers WHERE email=%s",
        [email],
    )
    user = cur.fetchone()
    close(conn, cur)
    return user


def add_surfboard(
    shaper_id,
    model_name,
    model_type,
    min_wave_size,
    max_wave_size,
    wave_type,
    break_type,
    skill_level,
    img_single,
    img_detail,
    surfboard_url,
):
    conn, cur = connect()
    cur.execute(
        "INSERT INTO surfboards (shaper_id, model_name, model_type, min_wave_size, max_wave_size, wave_type, break_type, skill_level, img_single, img_detail, surfboard_url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        [
            shaper_id,
            model_name,
            model_type,
            min_wave_size,
            max_wave_size,
            wave_type,
            break_type,
            skill_level,
            img_single,
            img_detail,
            surfboard_url,
        ],
    )
    conn.commit()
    close(conn, cur)


if __name__ == "__main__":
    # executes these func only when we can call the file directly: python3 model.py. Not when its imported as a module
    conn, cur = connect()
    create_tables("schema.sql")
    insert("seed.sql")
    close(conn, cur)
