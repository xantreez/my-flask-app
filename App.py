import sqlite3
from functools import wraps
from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

app = Flask(__name__)
app.secret_key = "secret_key_pro"


# Танзими пойгоҳи додаҳо (Database)
def create_database():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """
    )
    conn.commit()
    conn.close()


# Декоратор барои санҷиши воридшавӣ ба система
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_name" not in session:

            return redirect(url_for("login"))
        return f(*args, **kwargs)

    return decorated_function


# ---------------- LOGIN / REGISTER ----------------
@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password),
        )
        user = cursor.fetchone()
        conn.close()

        if user:
            session["user_name"] = username
            return redirect(url_for("dashboard"))
        else:
            flash("Номи корбар ё парол нодуруст аст!")

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        try:
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, password),
            )
            conn.commit()
            conn.close()
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            flash("Ин номи корбар аллакай мавҷуд аст!")

    return render_template("register.html")


# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
@login_required
def dashboard():
    lessons = [
        {"id": 1, "title": "What is Figma?", "description": "Introduction to Figma."},
        {"id": 2, "title": "Figma Tools", "description": "Overview of essential tools."},
        {"id": 3, "title": "Frame and Layout", "description": "Organize screens effectively."},
        {"id": 4, "title": "Components", "description": "Create reusable design elements."},
        {"id": 5, "title": "Prototype", "description": "Learn how to make your design interactive."},
    ]
    return render_template(
        "dashboard.html", lessons=lessons, user_name=session["user_name"]
    )


# ---------------- LESSON ----------------
@app.route("/lesson/<int:lesson_id>")
@login_required
def lesson(lesson_id):
    lessons = {
        1: {
            "title": "What is Figma?",
            "content": "Figma is a design tool used to create websites, mobile applications and user interfaces.",
        },
        2: {
            "title": "Figma Tools",
            "content": "Important Figma tools include Move, Frame, Text, Shape and Pen Tool.",
        },
        3: {
            "title": "Frame and Layout",
            "content": "Frames are used to create screens and organize your design.",
        },
        4: {
            "title": "Components",
            "content": "Components help you reuse the same elements in different parts of your design.",
        },
        5: {
            "title": "Prototype",
            "content": "Prototype allows you to connect screens and show how your application works.",
        },
    }
    selected_lesson = lessons.get(lesson_id)
    if not selected_lesson:
        return redirect(url_for("dashboard"))
    return render_template("lesson.html", lesson=selected_lesson)


# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


# ---------------- RUN WEBSITE ----------------
@app.route("/users")
def show_users():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, username FROM users")
    users_list = cursor.fetchall()
    conn.close()
    
    html = "<h1>Рӯйхати корбарон:</h1><ul>"
    for user in users_list:
        html += f"<li>ID: {user[0]} | Username: {user[1]}</li>"
    html += "</ul><a href='/dashboard'>← Бозгашт</a>"
    
    return html

if __name__ == "__main__":
    create_database()
    app.run(debug=True)