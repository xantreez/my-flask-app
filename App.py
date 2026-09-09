# import sqlite3
# from functools import wraps
# from flask import (
#     Flask,
#     flash,
#     redirect,
#     render_template,
#     request,
#     session,
#     url_for,
# )

# app = Flask(__name__)
# app.secret_key = "secret_key_pro"


# # Танзими пойгоҳи додаҳо (Database)
# def create_database():
#     conn = sqlite3.connect("database.db")
#     cursor = conn.cursor()
#     cursor.execute(
#         """
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             username TEXT UNIQUE NOT NULL,
#             password TEXT NOT NULL
#         )
#     """
#     )
#     conn.commit()
#     conn.close()


# # Эҷоди автоматикии база ҳангоми оғози сервер дар Render
# create_database()


# # Декоратор барои санҷиши воридшавӣ ба система
# def login_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if "user_name" not in session:
#             return redirect(url_for("login"))
#         return f(*args, **kwargs)

#     return decorated_function


# # ---------------- LOGIN / REGISTER ----------------
# @app.route("/", methods=["GET", "POST"])
# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         username = request.form.get("username")
#         password = request.form.get("password")

#         conn = sqlite3.connect("database.db")
#         cursor = conn.cursor()
#         cursor.execute(
#             "SELECT * FROM users WHERE username = ? AND password = ?",
#             (username, password),
#         )
#         user = cursor.fetchone()
#         conn.close()

#         if user:
#             session["user_name"] = username
#             return redirect(url_for("dashboard"))
#         else:
#             flash("Номи корбар ё парол нодуруст аст!")

#     return render_template("login.html")


# @app.route("/register", methods=["GET", "POST"])
# def register():
#     if request.method == "POST":
#         username = request.form.get("username")
#         password = request.form.get("password")

#         try:
#             conn = sqlite3.connect("database.db")
#             cursor = conn.cursor()
#             cursor.execute(
#                 "INSERT INTO users (username, password) VALUES (?, ?)",
#                 (username, password),
#             )
#             conn.commit()
#             conn.close()
#             return redirect(url_for("login"))
#         except sqlite3.IntegrityError:
#             flash("Ин номи корбар аллакай мавҷуд аст!")

#     return render_template("register.html")


# # ---------------- DASHBOARD ----------------
# @app.route("/dashboard")
# @login_required
# def dashboard():
#     lessons = [
#         {"id": 1, "title": "What is Figma?", "description": "Introduction to Figma."},
#         {"id": 2, "title": "Figma Tools", "description": "Overview of essential tools."},
#         {"id": 3, "title": "Frame and Layout", "description": "Organize screens effectively."},
#         {"id": 4, "title": "Components", "description": "Create reusable design elements."},
#         {"id": 5, "title": "Prototype", "description": "Learn how to make your design interactive."},
#     ]
#     return render_template(
#         "dashboard.html", lessons=lessons, user_name=session["user_name"]
#     )


# # ---------------- LESSON ----------------
# @app.route("/lesson/<int:lesson_id>")
# @login_required
# def lesson(lesson_id):
#     lessons = {
#         1: {
#             "title": "What is Figma?",
#             "content": "Figma is a design tool used to create websites, mobile applications and user interfaces.",
#         },
#         2: {
#             "title": "Figma Tools",
#             "content": "Important Figma tools include Move, Frame, Text, Shape and Pen Tool.",
#         },
#         3: {
#             "title": "Frame and Layout",
#             "content": "Frames are used to create screens and organize your design.",
#         },
#         4: {
#             "title": "Components",
#             "content": "Components help you reuse the same elements in different parts of your design.",
#         },
#         5: {
#             "title": "Prototype",
#             "content": "Prototype allows you to connect screens and show how your application works.",
#         },
#     }
#     selected_lesson = lessons.get(lesson_id)
#     if not selected_lesson:
#         return redirect(url_for("dashboard"))
#     return render_template("lesson.html", lesson=selected_lesson)


# # ---------------- LOGOUT ----------------
# @app.route("/logout")
# def logout():
#     session.clear()
#     return redirect(url_for("login"))


# # ---------------- SHOW USERS ----------------
# @app.route("/users")
# def show_users():
#     conn = sqlite3.connect("database.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT id, username FROM users")
#     users_list = cursor.fetchall()
#     conn.close()

#     html = "<h1>Рӯйхати корбарон:</h1><ul>"
#     for user in users_list:
#         html += f"<li>ID: {user[0]} | Username: {user[1]}</li>"
#     html += "</ul><a href='/dashboard'>← Бозгашт</a>"

#     return html


# # ---------------- RUN LOCAL ----------------
# if __name__ == "__main__":
#     create_database()
#     app.run(debug=True)
# import sqlite3
# from functools import wraps
# from flask import (
#     Flask,
#     flash,
#     redirect,
#     render_template,
#     request,
#     session,
#     url_for,
# )

# app = Flask(__name__)
# app.secret_key = "secret_key_pro"


# # Танзими пойгоҳи додаҳо (Database)
# def create_database():
#     conn = sqlite3.connect("database.db")
#     cursor = conn.cursor()
#     cursor.execute(
#         """
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             username TEXT UNIQUE NOT NULL,
#             password TEXT NOT NULL
#         )
#     """
#     )
#     conn.commit()
#     conn.close()


# create_database()


# def login_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if "user_name" not in session:
#             return redirect(url_for("login"))
#         return f(*args, **kwargs)

#     return decorated_function


# # ---------------- LOGIN / REGISTER ----------------
# @app.route("/", methods=["GET", "POST"])
# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         username = request.form.get("username")
#         password = request.form.get("password")

#         conn = sqlite3.connect("database.db")
#         cursor = conn.cursor()
#         cursor.execute(
#             "SELECT * FROM users WHERE username = ? AND password = ?",
#             (username, password),
#         )
#         user = cursor.fetchone()
#         conn.close()

#         if user:
#             session["user_name"] = username
#             return redirect(url_for("dashboard"))
#         else:
#             flash("Номи корбар ё парол нодуруст аст!")

#     return render_template("login.html")


# @app.route("/register", methods=["GET", "POST"])
# def register():
#     if request.method == "POST":
#         username = request.form.get("username")
#         password = request.form.get("password")

#         try:
#             conn = sqlite3.connect("database.db")
#             cursor = conn.cursor()
#             cursor.execute(
#                 "INSERT INTO users (username, password) VALUES (?, ?)",
#                 (username, password),
#             )
#             conn.commit()
#             conn.close()
#             return redirect(url_for("login"))
#         except sqlite3.IntegrityError:
#             flash("Ин номи корбар аллакай мавҷуд аст!")

#     return render_template("register.html")


# # ---------------- DASHBOARD ----------------
# @app.route("/dashboard")
# @login_required
# def dashboard():
#     lessons = [
#         {"id": 1, "title": "What is Figma?", "description": "Introduction to Figma and cloud-based design."},
#         {"id": 2, "title": "Figma Tools", "description": "Overview of essential UI elements and toolbars."},
#         {"id": 3, "title": "Frame and Layout", "description": "Organize screens and device templates effectively."},
#         {"id": 4, "title": "Components", "description": "Create reusable design assets and UI kits."},
#         {"id": 5, "title": "Prototype", "description": "Learn how to make your design interactive."},
#         {"id": 6, "title": "Shapes & Pen Tool", "description": "Create custom vector graphics and icons."},
#         {"id": 7, "title": "Text & Typography", "description": "Work with fonts, line heights, and text styles."},
#         {"id": 8, "title": "Auto Layout Basics", "description": "Build dynamic, flexible responsive UI components."},
#         {"id": 9, "title": "Colors & Styles", "description": "Manage global design system colors and shadows."},
#         {"id": 10, "title": "Exporting Assets", "description": "Export assets and prepare design for developers."},
#         {"id": 11, "title": "Advanced Prototyping", "description": "Smart animate, interactive overlays, and scrolling."},
#         {"id": 12, "title": "Design Systems", "description": "Building and publishing Figma library UI components."},
#         {"id": 13, "title": "UI Animation", "description": "Micro-interactions and motion design in Figma."},
#         {"id": 14, "title": "Responsive Layouts", "description": "Designing for Mobile, Tablet, and Desktop screens."},
#         {"id": 15, "title": "Final Portfolio Project", "description": "Creating a complete real-world mobile app UI design."}
#     ]
#     return render_template(
#         "dashboard.html", lessons=lessons, user_name=session["user_name"]
#     )


# # ---------------- LESSON ----------------
# @app.route("/lesson/<int:lesson_id>")
# @login_required
# def lesson(lesson_id):
#     lessons = {
#         1: {"title": "What is Figma?", "content": "Figma is a cloud-based UI/UX design and prototyping tool."},
#         2: {"title": "Figma Tools", "content": "Learn tools: Move, Scale, Frame, Section, Shape, Pen, Text."},
#         3: {"title": "Frame and Layout", "content": "Frames act as screen containers for responsive design layout."},
#         4: {"title": "Components", "content": "Master Master Components and Instances for design systems."},
#         5: {"title": "Prototype", "content": "Connect frames using triggers, transitions, and hover states."},
#         6: {"title": "Shapes & Pen Tool", "content": "Vector editing, boolean groups (Union, Subtract), and custom icon creation."},
#         7: {"title": "Text & Typography", "content": "Google Fonts integration, line-height, letter spacing, and text styles."},
#         8: {"title": "Auto Layout Basics", "content": "Create auto-resizing buttons, lists, and dynamic card layouts."},
#         9: {"title": "Colors & Styles", "content": "Create color variables, gradients, and layer styles for consistency."},
#         10: {"title": "Exporting Assets", "content": "Export PNG, SVG, JPG, PDF assets and developer handoff specs."},
#         11: {"title": "Advanced Prototyping", "content": "Use Smart Animate, Drag triggers, and interactive component states."},
#         12: {"title": "Design Systems", "content": "Organize variant properties, tokens, and team library components."},
#         13: {"title": "UI Animation", "content": "Animate loader buttons, toggle switches, and page transitions."},
#         14: {"title": "Responsive Layouts", "content": "Use constraints, auto layout wrapping, and breakpoints for screens."},
#         15: {"title": "Final Portfolio Project", "content": "Combine all skills to design a complete multi-screen app design!"}
#     }
#     selected_lesson = lessons.get(lesson_id)
#     if not selected_lesson:
#         return redirect(url_for("dashboard"))
#     return render_template("lesson.html", lesson=selected_lesson)


# # ---------------- LOGOUT ----------------
# @app.route("/logout")
# def logout():
#     session.clear()
#     return redirect(url_for("login"))


# # ---------------- SHOW USERS ----------------
# @app.route("/users")
# def show_users():
#     conn = sqlite3.connect("database.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT id, username FROM users")
#     users_list = cursor.fetchall()
#     conn.close()

#     html = "<h1>Рӯйхати корбарон:</h1><ul>"
#     for user in users_list:
#         html += f"<li>ID: {user[0]} | Username: {user[1]}</li>"
#     html += "</ul><a href='/dashboard'>← Бозгашт</a>"

#     return html


# # ---------------- RUN LOCAL ----------------
# if __name__ == "__main__":
#     create_database()
#     app.run(debug=True)


# import os
# from functools import wraps
# from flask import (
#     Flask,
#     flash,
#     redirect,
#     render_template,
#     request,
#     session,
#     url_for,
# )

# from flask_sqlalchemy import SQLAlchemy
 
# app = Flask(__name__)
#  app.secret_key = os.environ.get("SECRET_KEY", "secret_key_pro")
 
# # ---------------- DATABASE CONFIG ----------------
# # Render automatically provides a DATABASE_URL env var when you attach a
# # PostgreSQL instance to this service. Locally (no DATABASE_URL set), it
# # falls back to a SQLite file so you can still develop on your machine.
# database_url = os.environ.get("DATABASE_URL", "sqlite:///database.db")
 
# # Render's DATABASE_URL starts with "postgres://" but SQLAlchemy needs
# # "postgresql://" — this line fixes that automatically.
# if database_url.startswith("postgres://"):
#     database_url = database_url.replace("postgres://", "postgresql://", 1)
 
# app.config["SQLALCHEMY_DATABASE_URI"] = database_url
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
 
# db = SQLAlchemy(app)
 
 
# # ---------------- MODEL ----------------
# class User(db.Model):
#     __tablename__ = "users"
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(150), unique=True, nullable=False)
#     password = db.Column(db.String(150), nullable=False)
 
 
# with app.app_context():
#     db.create_all()
 
 
# # ---------------- LOGIN DECORATOR ----------------
# def login_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if "user_name" not in session:
#             return redirect(url_for("login"))
#         return f(*args, **kwargs)
 
#     return decorated_function
 
 
# # ---------------- LOGIN / REGISTER ----------------
# @app.route("/", methods=["GET", "POST"])
# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         username = request.form.get("username")
#         password = request.form.get("password")
 
#         user = User.query.filter_by(username=username, password=password).first()
 
#         if user:
#             session["user_name"] = username
#             return redirect(url_for("dashboard"))
#         else:
#             flash("Номи корбар ё парол нодуруст аст!")
 
#     return render_template("login.html")
 
 
# @app.route("/register", methods=["GET", "POST"])
# def register():
#     if request.method == "POST":
#         username = request.form.get("username")
#         password = request.form.get("password")
 
#         existing_user = User.query.filter_by(username=username).first()
#         if existing_user:
#             flash("Ин номи корбар аллакай мавҷуд аст!")
#         else:
#             new_user = User(username=username, password=password)
#             db.session.add(new_user)
#             db.session.commit()
#             return redirect(url_for("login"))
 
#     return render_template("register.html")
 
 
# # ---------------- DASHBOARD ----------------
# @app.route("/dashboard")
# @login_required
# def dashboard():
#     lessons = [
#         {"id": 1, "title": "What is Figma?", "description": "Introduction to Figma and cloud-based design."},
#         {"id": 2, "title": "Figma Tools", "description": "Overview of essential UI elements and toolbars."},
#         {"id": 3, "title": "Frame and Layout", "description": "Organize screens and device templates effectively."},
#         {"id": 4, "title": "Components", "description": "Create reusable design assets and UI kits."},
#         {"id": 5, "title": "Prototype", "description": "Learn how to make your design interactive."},
#         {"id": 6, "title": "Shapes & Pen Tool", "description": "Create custom vector graphics and icons."},
#         {"id": 7, "title": "Text & Typography", "description": "Work with fonts, line heights, and text styles."},
#         {"id": 8, "title": "Auto Layout Basics", "description": "Build dynamic, flexible responsive UI components."},
#         {"id": 9, "title": "Colors & Styles", "description": "Manage global design system colors and shadows."},
#         {"id": 10, "title": "Exporting Assets", "description": "Export assets and prepare design for developers."},
#         {"id": 11, "title": "Advanced Prototyping", "description": "Smart animate, interactive overlays, and scrolling."},
#         {"id": 12, "title": "Design Systems", "description": "Building and publishing Figma library UI components."},
#         {"id": 13, "title": "UI Animation", "description": "Micro-interactions and motion design in Figma."},
#         {"id": 14, "title": "Responsive Layouts", "description": "Designing for Mobile, Tablet, and Desktop screens."},
#         {"id": 15, "title": "Final Portfolio Project", "description": "Creating a complete real-world mobile app UI design."}
#     ]
#     return render_template(
#         "dashboard.html", lessons=lessons, user_name=session["user_name"]
#     )
 
 
# # ---------------- LESSON ----------------
# @app.route("/lesson/<int:lesson_id>")
# @login_required
# def lesson(lesson_id):
#     lessons = {
#         1: {"title": "What is Figma?", "content": "Figma is a cloud-based UI/UX design and prototyping tool."},
#         2: {"title": "Figma Tools", "content": "Learn tools: Move, Scale, Frame, Section, Shape, Pen, Text."},
#         3: {"title": "Frame and Layout", "content": "Frames act as screen containers for responsive design layout."},
#         4: {"title": "Components", "content": "Master Master Components and Instances for design systems."},
#         5: {"title": "Prototype", "content": "Connect frames using triggers, transitions, and hover states."},
#         6: {"title": "Shapes & Pen Tool", "content": "Vector editing, boolean groups (Union, Subtract), and custom icon creation."},
#         7: {"title": "Text & Typography", "content": "Google Fonts integration, line-height, letter spacing, and text styles."},
#         8: {"title": "Auto Layout Basics", "content": "Create auto-resizing buttons, lists, and dynamic card layouts."},
#         9: {"title": "Colors & Styles", "content": "Create color variables, gradients, and layer styles for consistency."},
#         10: {"title": "Exporting Assets", "content": "Export PNG, SVG, JPG, PDF assets and developer handoff specs."},
#         11: {"title": "Advanced Prototyping", "content": "Use Smart Animate, Drag triggers, and interactive component states."},
#         12: {"title": "Design Systems", "content": "Organize variant properties, tokens, and team library components."},
#         13: {"title": "UI Animation", "content": "Animate loader buttons, toggle switches, and page transitions."},
#         14: {"title": "Responsive Layouts", "content": "Use constraints, auto layout wrapping, and breakpoints for screens."},
#         15: {"title": "Final Portfolio Project", "content": "Combine all skills to design a complete multi-screen app design!"}
#     }
#     selected_lesson = lessons.get(lesson_id)
#     if not selected_lesson:
#         return redirect(url_for("dashboard"))
#     return render_template("lesson.html", lesson=selected_lesson)
 
 
# # ---------------- LOGOUT ----------------
# @app.route("/logout")
# def logout():
#     session.clear()
#     return redirect(url_for("login"))
 
 
# # ---------------- SHOW USERS ----------------
# @app.route("/users")
# def show_users():
#     users_list = User.query.all()
 
#     html = "<h1>Рӯйхати корбарон:</h1><ul>"
#     for user in users_list:
#         html += f"<li>ID: {user.id} | Username: {user.username}</li>"
#     html += "</ul><a href='/dashboard'>← Бозгашт</a>"
 
#     return html
 
 
# # ---------------- RUN LOCAL ----------------
# if __name__ == "__main__":
#     app.run(debug=True)
 
import os
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
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "secret_key_pro")

# ---------------- DATABASE CONFIG ----------------
database_url = os.environ.get("DATABASE_URL", "sqlite:///database.db")
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# ---------------- MODEL ----------------
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)


with app.app_context():
    db.create_all()


# ---------------- LOGIN DECORATOR ----------------
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_name" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)

    return decorated_function


# ---------------- LOGIN / REGISTER ----------------
@app.route("/", methods=["GET", "POST"])
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Ин номи корбар аллакай мавҷуд аст!")
        else:
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username, password=password).first()

        if user:
            session["user_name"] = username
            return redirect(url_for("dashboard"))
        else:
            flash("Номи корбар ё парол нодуруст аст!")

    return render_template("login.html")


# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
@login_required
def dashboard():
    lessons = [
        {"id": 1, "title": "What is Figma?", "description": "Introduction to Figma and cloud-based design."},
        {"id": 2, "title": "Figma Tools", "description": "Overview of essential UI elements and toolbars."},
        {"id": 3, "title": "Frame and Layout", "description": "Organize screens and device templates effectively."},
        {"id": 4, "title": "Components", "description": "Create reusable design assets and UI kits."},
        {"id": 5, "title": "Prototype", "description": "Learn how to make your design interactive."},
        {"id": 6, "title": "Shapes & Pen Tool", "description": "Create custom vector graphics and icons."},
        {"id": 7, "title": "Text & Typography", "description": "Work with fonts, line heights, and text styles."},
        {"id": 8, "title": "Auto Layout Basics", "description": "Build dynamic, flexible responsive UI components."},
        {"id": 9, "title": "Colors & Styles", "description": "Manage global design system colors and shadows."},
        {"id": 10, "title": "Exporting Assets", "description": "Export assets and prepare design for developers."},
        {"id": 11, "title": "Advanced Prototyping", "description": "Smart animate, interactive overlays, and scrolling."},
        {"id": 12, "title": "Design Systems", "description": "Building and publishing Figma library UI components."},
        {"id": 13, "title": "UI Animation", "description": "Micro-interactions and motion design in Figma."},
        {"id": 14, "title": "Responsive Layouts", "description": "Designing for Mobile, Tablet, and Desktop screens."},
        {"id": 15, "title": "Final Portfolio Project", "description": "Creating a complete real-world mobile app UI design."}
    ]
    return render_template(
        "dashboard.html", lessons=lessons, user_name=session["user_name"]
    )


# ---------------- LESSON ----------------
@app.route("/lesson/<int:lesson_id>")
@login_required
def lesson(lesson_id):
    lessons = {
        1: {"title": "What is Figma?", "content": "Figma is a cloud-based UI/UX design and prototyping tool."},
        2: {"title": "Figma Tools", "content": "Learn tools: Move, Scale, Frame, Section, Shape, Pen, Text."},
        3: {"title": "Frame and Layout", "content": "Frames act as screen containers for responsive design layout."},
        4: {"title": "Components", "content": "Master Master Components and Instances for design systems."},
        5: {"title": "Prototype", "content": "Connect frames using triggers, transitions, and hover states."},
        6: {"title": "Shapes & Pen Tool", "content": "Vector editing, boolean groups (Union, Subtract), and custom icon creation."},
        7: {"title": "Text & Typography", "content": "Google Fonts integration, line-height, letter spacing, and text styles."},
        8: {"title": "Auto Layout Basics", "content": "Create auto-resizing buttons, lists, and dynamic card layouts."},
        9: {"title": "Colors & Styles", "content": "Create color variables, gradients, and layer styles for consistency."},
        10: {"title": "Exporting Assets", "content": "Export PNG, SVG, JPG, PDF assets and developer handoff specs."},
        11: {"title": "Advanced Prototyping", "content": "Use Smart Animate, Drag triggers, and interactive component states."},
        12: {"title": "Design Systems", "content": "Organize variant properties, tokens, and team library components."},
        13: {"title": "UI Animation", "content": "Animate loader buttons, toggle switches, and page transitions."},
        14: {"title": "Responsive Layouts", "content": "Use constraints, auto layout wrapping, and breakpoints for screens."},
        15: {"title": "Final Portfolio Project", "content": "Combine all skills to design a complete multi-screen app design!"}
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


# ---------------- SHOW USERS ----------------
@app.route("/users")
@login_required
def show_users():
    users_list = User.query.order_by(User.id.desc()).all()
    return render_template("users.html", users=users_list)


# ---------------- RUN LOCAL ----------------
if __name__ == "__main__":
    app.run(debug=True)