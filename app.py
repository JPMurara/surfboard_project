from flask import Flask, render_template, request, flash, redirect, session
import os
import psycopg2
from model import connect, close, insert_shaper, get_user, search, add_surfboard
import bcrypt

app = Flask(__name__)
app.secret_key = "secret_key"


@app.route("/")
def index():
    return render_template("index.html.jinja")


@app.route("/search", methods=["GET"])
def select_surfboard():
    min_wave_size = request.args.get("min_wave_size")
    max_wave_size = request.args.get("max_wave_size")
    wave_type = request.args.get("wave_type")
    break_type = request.args.get("break_type")
    skill_level = request.args.get("skill_level")

    exact_match = search(
        min_wave_size, max_wave_size, wave_type, break_type, skill_level
    )

    return render_template(
        "results.html.jinja",
        exact_match=exact_match,
    )


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
    shaper_url = request.form.get("shaper-url")
    password = request.form.get("password")
    confirm_password = request.form.get("confirm-password")
    if password == confirm_password:
        binary_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        # binary password is binary, need to be a string to store in the DB
        # decode() - converts from binary to string to be able to store in the DB
        password_hash = binary_password.decode()
        insert_shaper(shaper_name, email, shaper_url, password_hash)
        return redirect("/login")
    else:
        flash("Passwords don't match. Please try again.", "error")
        return redirect("/register")


@app.route("/login")
def login():
    if not session.get("user"):
        return render_template("login.html.jinja")
    else:
        return redirect("/")


@app.route("/login_action", methods=["POST"])
def login_action():
    if not session.get("user"):
        email = request.form.get("email")
        password = request.form.get("password")
        user = get_user(email)
        if not user:
            flash("User not registered yet. Please sign up", "error")
            return redirect("/register")
        id, shaper_name, _, _, is_admin, password_hash = user
        valid = bcrypt.checkpw(password.encode(), user["password_hash"].encode())
        if valid:
            session["user"] = {
                "name": user["shaper_name"],
                "shaper_id": user["id"],
                "is_admin": user["is_admin"],
            }
            return redirect("/")
        else:
            flash("Username or Passwords is wrong. Please try again.", "error")
            return redirect("/login")
    else:
        return redirect("/")


@app.route("/logout", methods=["POST"])
def logout():
    if session.get("user"):
        if request.method == "POST":
            session.clear()
            return redirect("/")
        else:
            return redirect("/")


@app.route("/add")
def add():
    if session.get("user") and session["user"]["is_admin"] == True:
        return render_template("add.html.jinja")
    else:
        return redirect("/")


@app.route("/add_action", methods=["POST"])
def add_action():
    shaper_id = session["user"]["shaper_id"]
    model_name = request.form.get("model-name")
    model_type = request.form.get("model-type")
    min_wave_size = int(request.form.get("min-wave-size"))
    max_wave_size = int(request.form.get("max-wave-size"))
    wave_type = request.form.get("wave-type")
    break_type = request.form.get("break-type")
    skill_level = request.form.get("skill-level")
    img_single = request.form.get("img-single")
    img_detail = request.form.get("img-detail")
    surfboard_url = request.form.get("surfboard-url")

    add_surfboard(
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
    )
    return redirect("/")

@app.route("/about")
def about():
    return render_template("about.html.jinja")

if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
