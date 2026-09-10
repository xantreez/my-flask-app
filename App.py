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
# app.secret_key = os.environ.get("SECRET_KEY", "secret_key_pro")

# # ---------------- DATABASE CONFIG ----------------
# database_url = os.environ.get("DATABASE_URL", "sqlite:///database.db")
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
# @login_required
# def show_users():
#     users_list = User.query.order_by(User.id.desc()).all()
#     return render_template("users.html", users=users_list)


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
        1: {
            "title": "What is Figma?",
            "time": "10 дақиқа",
            "intro": "Figma is a cloud-based UI/UX design and prototyping tool used by teams around the world to design apps and websites collaboratively in real time.",
            "objectives": [
                "Тавзеҳ диҳед, ки Figma чист ва барои чӣ истифода мешавад",
                "Фарқияти он аз абзорҳои дигари дизайн (масалан Photoshop)-ро фаҳмед",
                "Интерфейси асосии Figma-ро шинос шавед"
            ],
            "takeaways": [
                "Figma дар браузер кор мекунад — ниёз ба насб нест",
                "Якчанд нафар метавонанд ҳамзамон дар як файл кор кунанд",
                "Файлҳо худкор дар cloud захира мешаванд"
            ]
        },
        2: {
            "title": "Figma Tools",
            "time": "12 дақиқа",
            "intro": "Learn the essential toolbar: Move, Scale, Frame, Section, Shape, Pen, and Text tools that form the foundation of every design.",
            "objectives": [
                "Абзорҳои асосии toolbar-ро номбар кунед",
                "Фарқияти Move ва Scale tool-ро фаҳмед",
                "Кай кадом абзорро истифода баред донед"
            ],
            "takeaways": [
                "Ҳар абзор кнопкаи миёнбур (shortcut) дорад — истифодаи онҳо суръатро зиёд мекунад",
                "Frame tool барои сохтани экранҳо асос аст",
                "Pen tool барои шаклҳои мураккаб истифода мешавад"
            ]
        },
        3: {
            "title": "Frame and Layout",
            "time": "12 дақиқа",
            "intro": "Frames act as screen containers that organize your design and let you build responsive layouts for different device sizes.",
            "objectives": [
                "Фарқияти Frame ва Group-ро фаҳмед",
                "Андозаҳои стандартии device (mobile, tablet, desktop)-ро донед",
                "Layout-и экранҳоро мураттаб созед"
            ],
            "takeaways": [
                "Frame метавонад дигар Frame-ҳоро дар дохили худ дошта бошад",
                "Presets барои андозаҳои маъмултарин мавҷуданд",
                "Номгузории дурусти frame-ҳо кори дастаҷамъиро осон мекунад"
            ]
        },
        4: {
            "title": "Components",
            "time": "15 дақиқа",
            "intro": "Components let you create reusable design elements — build once, use everywhere, and update all instances at the same time.",
            "objectives": [
                "Фарқияти Master Component ва Instance-ро фаҳмед",
                "Компоненти истифодашавандаро эҷод кунед",
                "Тағйиротро дар як ҷо кунед, то дар ҳама ҷо иваз шавад"
            ],
            "takeaways": [
                "Тағйирот дар Master ба ҳамаи Instance-ҳо таъсир мекунад",
                "Instance-ҳоро метавон бе вайрон кардани Master фардикунонӣ кард",
                "Компонентҳо асоси системаи дизайн (Design System) мебошанд"
            ]
        },
        5: {
            "title": "Prototype",
            "time": "15 дақиқа",
            "intro": "Prototype mode lets you connect frames using triggers, transitions, and hover states to simulate how your app will actually work.",
            "objectives": [
                "Фреймҳоро тавассути interaction пайваст кунед",
                "Намудҳои trigger (click, hover, drag)-ро фаҳмед",
                "Тарзи ҳаракати намунавии барномаро сохта тавонед"
            ],
            "takeaways": [
                "Prototype барои нишон додани идея ба мизоҷ хеле муфид аст",
                "Transition-ҳо ҳаракатро табиитар месозанд",
                "Presentation mode барои санҷиши прототип истифода мешавад"
            ]
        },
        6: {
            "title": "Shapes & Pen Tool",
            "time": "14 дақиқа",
            "intro": "Master vector editing with boolean groups (Union, Subtract, Intersect) to create custom icons and illustrations.",
            "objectives": [
                "Бо Pen tool шаклҳои дилхоҳ сохта тавонед",
                "Амалиёти Boolean (Union, Subtract, Intersect)-ро фаҳмед",
                "Icon-и худиатонро сохта тавонед"
            ],
            "takeaways": [
                "Vector shape-ҳо бе гум кардани сифат калон мешаванд",
                "Boolean groups якчанд shape-ро ба як шакли нав табдил медиҳанд",
                "Pen tool ниёз ба тамрин дорад, вале хеле пурқувват аст"
            ]
        },
        7: {
            "title": "Text & Typography",
            "time": "10 дақиқа",
            "intro": "Work with Google Fonts, line-height, letter spacing, and reusable text styles to keep your typography consistent.",
            "objectives": [
                "Font, line-height ва letter-spacing-ро танзим кунед",
                "Text style-и истифодашавандаро эҷод кунед",
                "Иерархияи матниро (h1, h2, body) фаҳмед"
            ],
            "takeaways": [
                "Text style монанди компонент — тағйирот дар ҳама ҷо инъикос меёбад",
                "Line-height хониши матнро беҳтар мекунад",
                "Истифодаи на бештар аз 2 font дар як лоиҳа тавсия мешавад"
            ]
        },
        8: {
            "title": "Auto Layout Basics",
            "time": "15 дақиқа",
            "intro": "Build auto-resizing buttons, lists, and dynamic card layouts using Auto Layout — Figma's most powerful feature for responsive design.",
            "objectives": [
                "Auto Layout-ро ба frame илова кунед",
                "Padding ва spacing-ро танзим кунед",
                "Card ё button-и худкор-андозашавандаро сохта тавонед"
            ],
            "takeaways": [
                "Auto Layout вақти дизайнро назаррас кам мекунад",
                "Тағйир додани матн андозаи элементро худкор иваз мекунад",
                "Ин асоси responsive design дар Figma аст"
            ]
        },
        9: {
            "title": "Colors & Styles",
            "time": "12 дақиқа",
            "intro": "Create color variables, gradients, and layer styles to maintain visual consistency across your entire design system.",
            "objectives": [
                "Color style-и истифодашавандаро эҷод кунед",
                "Gradient ва shadow-ро танзим кунед",
                "Палитаи рангии мутобиқро созед"
            ],
            "takeaways": [
                "Color style-ҳо тағйир додани ранги брендро осон мекунанд",
                "Shadow-ҳо ба элементҳо чуқурӣ (depth) медиҳанд",
                "Палитаи маҳдуд дизайнро касбитар нишон медиҳад"
            ]
        },
        10: {
            "title": "Exporting Assets",
            "time": "10 дақиқа",
            "intro": "Export PNG, SVG, JPG, and PDF assets, and prepare clean developer handoff specs for your engineering team.",
            "objectives": [
                "Формати дурусти export (PNG/SVG/PDF)-ро интихоб кунед",
                "Assets-ро бо резолюсияи гуногун (1x, 2x, 3x) содир кунед",
                "Handoff барои dev team-ро омода кунед"
            ],
            "takeaways": [
                "SVG барои icon беҳтарин интихоб аст (scalable)",
                "PNG барои тасвирҳои мураккаб бо шаффофӣ мувофиқ аст",
                "Dev Mode-и Figma ба муҳандисон CSS/spacing медиҳад"
            ]
        },
        11: {
            "title": "Advanced Prototyping",
            "time": "16 дақиқа",
            "intro": "Use Smart Animate, drag triggers, and interactive component states to build prototypes that feel like a real app.",
            "objectives": [
                "Smart Animate-ро байни ду frame татбиқ кунед",
                "Drag trigger-ро барои swipe/scroll истифода баред",
                "Interactive component (масалан checkbox, toggle)-ро созед"
            ],
            "takeaways": [
                "Smart Animate ба object-ҳои ҳамном автоматан animation медиҳад",
                "Overlay барои modal ва menu истифода мешавад",
                "Прототипи хуб бовариро назди мизоҷ баланд мекунад"
            ]
        },
        12: {
            "title": "Design Systems",
            "time": "18 дақиқа",
            "intro": "Organize variant properties, design tokens, and shared team libraries to scale your design work across a whole product.",
            "objectives": [
                "Component variant-ро сохта тавонед",
                "Design token (ранг, андоза, spacing)-ро ташкил кунед",
                "Library-и дастаҷамъиро дар лоиҳа паҳн кунед"
            ],
            "takeaways": [
                "Design System вақти такрории дизайнро кам мекунад",
                "Variant якчанд ҳолати як компонентро дар як ҷо ҷамъ мекунад",
                "Team library имкон медиҳад ҳамаи аъзоён як манбаъ истифода баранд"
            ]
        },
        13: {
            "title": "UI Animation",
            "time": "14 дақиқа",
            "intro": "Animate loader buttons, toggle switches, and page transitions to bring micro-interactions and motion design to your UI.",
            "objectives": [
                "Micro-interaction чист, фаҳмед",
                "Animation-и loader ва toggle-ро сохта тавонед",
                "Transition-ҳои саҳифаро мулоим кунед"
            ],
            "takeaways": [
                "Micro-interaction-ҳо таҷрибаи корбарро зинда мекунанд",
                "Animation набояд аз ҳад зиёд тӯл кашад (150–300ms беҳтарин)",
                "Easing (ease-in-out) ҳаракатро табиитар месозад"
            ]
        },
        14: {
            "title": "Responsive Layouts",
            "time": "16 дақиқа",
            "intro": "Use constraints, Auto Layout wrapping, and breakpoints to design screens that adapt across Mobile, Tablet, and Desktop.",
            "objectives": [
                "Constraint (pin ба чап/рост/боло/поён)-ро истифода баред",
                "Breakpoint барои андозаҳои гуногуни экран муайян кунед",
                "Тарҳро барои мобил ва десктоп мутобиқ созед"
            ],
            "takeaways": [
                "Constraints муайян мекунад, ки чӣ тавр элемент ҳангоми resize рафтор мекунад",
                "Design mobile-first одатан осонтар аст",
                "Auto Layout wrapping ба тарҳҳои responsive кӯмак мекунад"
            ]
        },
        15: {
            "title": "Final Portfolio Project",
            "time": "30+ дақиқа",
            "intro": "Combine everything you've learned to design a complete, multi-screen mobile app UI — ready for your portfolio.",
            "objectives": [
                "Ҳамаи малакаҳои омӯхтаро дар як лоиҳа истифода баред",
                "Аз идея то прототипи интерактивӣ пеш биравед",
                "Лоиҳаро барои portfolio омода кунед"
            ],
            "takeaways": [
                "Лоиҳаи portfolio беҳтарин роҳи нишон додани малака ба корфармост",
                "Мунтазам feedback гирифтан лоиҳаро беҳтар мекунад",
                "Ҳатто лоиҳаи хурд, агар пурра анҷом ёбад, арзишманд аст"
            ]
        }
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
 