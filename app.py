from flask import Flask, render_template, request, session, redirect, url_for
import os
import psycopg2
from model import connect, close

app = Flask(__name__)
app.secret_key = "secret_key"


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
        "SELECT * FROM surfboards WHERE min_wave_size<=%s OR max_wave_size>=%s AND wave_type=%s AND break_type=%s AND skill_level=%s",
        [min_wave_size, max_wave_size, wave_type, break_type, skill_level],
    )
    results = cur.fetchall()
    session["results"] = results
    print(cur.query)
    close(conn, cur)

    return redirect(url_for("surfboard_results"))


@app.route("/surfboard_results")
def results():
    results = session.get("results")

    # Check if results exist in the session
    if results is None:
        # Redirect to select_surfboard if no results are available
        return redirect(url_for("select_surfboard"))

    return render_template("results.html.jinja", results=results)


@app.route("/details")
def details():
    return render_template("details.html.jinja", results=results)


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
