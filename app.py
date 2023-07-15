from flask import Flask, render_template, request
import os
import psycopg2
from model import connect, close

app = Flask(__name__)


@app.route("/")
def index():
    # connection = psycopg2.connect(host=os.getenv("PGHOST"), user=os.getenv("PGUSER"), password=os.getenv("PGPASSWORD"), port=os.getenv("PGPORT"), dbname=os.getenv("PGDATABASE"))
    # connection = psycopg2.connect(os.getenv("DATABASE_URL", "dbname=surfboard_db"))
    # cursor = connection.cursor()
    # cursor.execute("SELECT * FROM surfboards;")
    # results = cursor.fetchall()
    # connection.close()
    # return f"{results[0]}"
    return render_template("index.html.jinja")


@app.route("/select_surfboard", methods=["GET"])
def select_surfboard():
    min_wave_size = request.args.get("min_wave_size")
    max_wave_size = request.args.get("max_wave_size")
    wave_type = request.args.get("wave_type")
    break_type = request.args.get("break_type")
    skill_level = request.args.get("skill_level")

    conn, cur = connect()

    cur.execute(
        "SELECT * FROM surfboards WHERE min_wave_size=%s AND max_wave_size=%s AND wave_type=%s AND break_type=%s AND skill_level=%s",
        [min_wave_size, max_wave_size, wave_type, break_type, skill_level],
    )
    results = cur.fetchall()
    print(cur.query)
    close(conn, cur)

    return render_template("results.html.jinja", results=results)


@app.route("/results")
def results():
    return render_template("results.html.jinja")


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
