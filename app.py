from flask import Flask, render_template, request, session, flash, redirect, url_for
import os
import psycopg2
from model import connect, close, insert_shaper
import bcrypt

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


@app.route("/search", methods=["GET"])
def select_surfboard():
    min_wave_size = request.args.get("min_wave_size")
    max_wave_size = request.args.get("max_wave_size")
    wave_type = request.args.get("wave_type")
    break_type = request.args.get("break_type")
    skill_level = request.args.get("skill_level")

    conn, cur = connect()

    cur.execute(
        "SELECT * FROM surfboards LEFT JOIN shapers ON surfboards.shaper_id = shapers.id WHERE min_wave_size<=%s OR max_wave_size>=%s AND wave_type=%s AND break_type=%s AND skill_level=%s",
        [min_wave_size, max_wave_size, wave_type, break_type, skill_level],
    )
    surfboard_results = cur.fetchall()

    close(conn, cur)

    return render_template("results.html.jinja", surfboard_results=surfboard_results)


@app.route("/results")
def results():
    return render_template("results.html.jinja", results=results)


@app.route("/register")
def register():
    return render_template("signup.html.jinja")


@app.route("/register_action", methods=["POST"])
def register_action():
    shaper_name = request.form.get("shaper-name")
    email = request.form.get("email")
    url = request.form.get("url")
    password = request.form.get("password")
    confirm_password = request.form.get("confirm-password")
    if password == confirm_password:
        binary_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        # binary password is binary, need to be a string to store in the DB
        # decode() - converts from binary to string to be able to store in the DB
        password_hash = binary_password.decode()
        insert_shaper(shaper_name, email, url, password_hash)
        return redirect("/login")
    else:
        flash("Passwords don't match. Please try again.", "error")
        return redirect("/signup")


@app.route("/login")
def login():
    return render_template("login.html.jinja")


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
