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
 
# ---------------------------------------------------------
# Database configuration
# Render provides DATABASE_URL automatically once a PostgreSQL
# instance is attached. Locally (no DATABASE_URL set), the app
# falls back to a SQLite file so it still works for development.
# ---------------------------------------------------------
database_url = os.environ.get("DATABASE_URL", "sqlite:///database.db")
 
# Render's DATABASE_URL starts with "postgres://" but SQLAlchemy
# requires "postgresql://" — this line fixes that automatically.
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)
 
app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
 
db = SQLAlchemy(app)
 
# The only account allowed to view the /users admin page.
# Set this in Render's Environment tab — never hardcode it here.
ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME")
 
 
# ---------------------------------------------------------
# Database model
# ---------------------------------------------------------
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
 
 
with app.app_context():
    db.create_all()
 
 
# ---------------------------------------------------------
# Access control decorators
# ---------------------------------------------------------
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_name" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
 
    return decorated_function
 
 
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_name" not in session:
            return redirect(url_for("login"))
        if not ADMIN_USERNAME or session["user_name"] != ADMIN_USERNAME:
            return redirect(url_for("dashboard"))
        return f(*args, **kwargs)
 
    return decorated_function
 
 
# ---------------------------------------------------------
# Auth routes — Register is the landing page, Login is separate
# ---------------------------------------------------------
@app.route("/", methods=["GET", "POST"])
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
 
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("This username already exists!")
        else:
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash("Account created successfully. Please log in.")
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
            flash("Incorrect username or password!")
 
    return render_template("login.html")
 
 
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))
 
 
# ---------------------------------------------------------
# Lesson content
# ---------------------------------------------------------
LESSONS = {
    1: {
        "title": "What is Figma?",
        "description": "Introduction to Figma and cloud-based design.",
        "time": "10 min",
        "intro": "Figma is a cloud-based UI/UX design and prototyping tool used by teams around the world to design apps and websites collaboratively in real time.",
        "objectives": [
            "Explain what Figma is and what it's used for",
            "Understand how it differs from tools like Photoshop",
            "Get familiar with the main Figma interface",
        ],
        "takeaways": [
            "Figma runs in the browser — no installation needed",
            "Multiple people can work in the same file at the same time",
            "Files are saved automatically to the cloud",
        ],
    },
    2: {
        "title": "Figma Tools",
        "description": "Overview of essential UI elements and toolbars.",
        "time": "12 min",
        "intro": "Learn the essential toolbar: Move, Scale, Frame, Section, Shape, Pen, and Text tools that form the foundation of every design.",
        "objectives": [
            "Name the core toolbar tools",
            "Understand the difference between Move and Scale",
            "Know when to use each tool",
        ],
        "takeaways": [
            "Every tool has a keyboard shortcut — learning them speeds up your workflow",
            "The Frame tool is the foundation for building screens",
            "The Pen tool is used for more complex custom shapes",
        ],
    },
    3: {
        "title": "Frame and Layout",
        "description": "Organize screens and device templates effectively.",
        "time": "12 min",
        "intro": "Frames act as screen containers that organize your design and let you build responsive layouts for different device sizes.",
        "objectives": [
            "Understand the difference between a Frame and a Group",
            "Know standard device sizes (mobile, tablet, desktop)",
            "Organize screen layouts cleanly",
        ],
        "takeaways": [
            "A Frame can contain other Frames inside it",
            "Presets exist for the most common screen sizes",
            "Naming frames clearly makes team collaboration easier",
        ],
    },
    4: {
        "title": "Components",
        "description": "Create reusable design assets and UI kits.",
        "time": "15 min",
        "intro": "Components let you create reusable design elements — build once, use everywhere, and update all instances at the same time.",
        "objectives": [
            "Understand the difference between a Main Component and an Instance",
            "Create a reusable component",
            "Update one place and see it reflect everywhere",
        ],
        "takeaways": [
            "Changes to the main component affect all instances",
            "Instances can be customized without breaking the main component",
            "Components are the foundation of any design system",
        ],
    },
    5: {
        "title": "Prototype",
        "description": "Learn how to make your design interactive.",
        "time": "15 min",
        "intro": "Prototype mode lets you connect frames using triggers, transitions, and hover states to simulate how your app will actually work.",
        "objectives": [
            "Connect frames together using interactions",
            "Understand trigger types (click, hover, drag)",
            "Build a working click-through prototype",
        ],
        "takeaways": [
            "Prototypes are great for presenting ideas to clients",
            "Transitions make interactions feel more natural",
            "Presentation mode is used to test the prototype",
        ],
    },
    6: {
        "title": "Shapes & Pen Tool",
        "description": "Create custom vector graphics and icons.",
        "time": "14 min",
        "intro": "Master vector editing with boolean groups (Union, Subtract, Intersect) to create custom icons and illustrations.",
        "objectives": [
            "Draw custom shapes with the Pen tool",
            "Understand boolean operations (Union, Subtract, Intersect)",
            "Create your own custom icon",
        ],
        "takeaways": [
            "Vector shapes scale up without losing quality",
            "Boolean groups combine multiple shapes into one new shape",
            "The Pen tool takes practice but is very powerful",
        ],
    },
    7: {
        "title": "Text & Typography",
        "description": "Work with fonts, line heights, and text styles.",
        "time": "10 min",
        "intro": "Work with Google Fonts, line-height, letter spacing, and reusable text styles to keep your typography consistent.",
        "objectives": [
            "Adjust font, line-height, and letter-spacing",
            "Create a reusable text style",
            "Understand text hierarchy (h1, h2, body)",
        ],
        "takeaways": [
            "Text styles work like components — one change updates everywhere",
            "Good line-height improves readability",
            "Using no more than 2 fonts per project is recommended",
        ],
    },
    8: {
        "title": "Auto Layout Basics",
        "description": "Build dynamic, flexible responsive UI components.",
        "time": "15 min",
        "intro": "Build auto-resizing buttons, lists, and dynamic card layouts using Auto Layout — Figma's most powerful feature for responsive design.",
        "objectives": [
            "Apply Auto Layout to a frame",
            "Adjust padding and spacing",
            "Build a self-resizing card or button",
        ],
        "takeaways": [
            "Auto Layout drastically reduces design time",
            "Changing text automatically resizes the element",
            "It's the foundation of responsive design in Figma",
        ],
    },
    9: {
        "title": "Colors & Styles",
        "description": "Manage global design system colors and shadows.",
        "time": "12 min",
        "intro": "Create color variables, gradients, and layer styles to maintain visual consistency across your entire design system.",
        "objectives": [
            "Create a reusable color style",
            "Configure gradients and shadows",
            "Build a consistent color palette",
        ],
        "takeaways": [
            "Color styles make rebranding a project much easier",
            "Shadows add depth to elements",
            "A limited palette makes a design look more professional",
        ],
    },
    10: {
        "title": "Exporting Assets",
        "description": "Export assets and prepare design for developers.",
        "time": "10 min",
        "intro": "Export PNG, SVG, JPG, and PDF assets, and prepare clean developer handoff specs for your engineering team.",
        "objectives": [
            "Choose the right export format (PNG/SVG/PDF)",
            "Export assets at multiple resolutions (1x, 2x, 3x)",
            "Prepare a clean developer handoff",
        ],
        "takeaways": [
            "SVG is the best choice for icons (fully scalable)",
            "PNG is best for complex images that need transparency",
            "Figma's Dev Mode gives engineers CSS and spacing values",
        ],
    },
    11: {
        "title": "Advanced Prototyping",
        "description": "Smart animate, interactive overlays, and scrolling.",
        "time": "16 min",
        "intro": "Use Smart Animate, drag triggers, and interactive component states to build prototypes that feel like a real app.",
        "objectives": [
            "Apply Smart Animate between two frames",
            "Use drag triggers for swipe/scroll interactions",
            "Build interactive components (e.g. checkbox, toggle)",
        ],
        "takeaways": [
            "Smart Animate automatically animates matching objects",
            "Overlays are used for modals and menus",
            "A polished prototype builds more trust with clients",
        ],
    },
    12: {
        "title": "Design Systems",
        "description": "Building and publishing Figma library UI components.",
        "time": "18 min",
        "intro": "Organize variant properties, design tokens, and shared team libraries to scale your design work across a whole product.",
        "objectives": [
            "Build component variants",
            "Organize design tokens (color, size, spacing)",
            "Publish a shared library across a project",
        ],
        "takeaways": [
            "A design system reduces repetitive design work",
            "Variants group multiple states of one component together",
            "Team libraries let everyone work from a single source of truth",
        ],
    },
    13: {
        "title": "UI Animation",
        "description": "Micro-interactions and motion design in Figma.",
        "time": "14 min",
        "intro": "Animate loader buttons, toggle switches, and page transitions to bring micro-interactions and motion design to your UI.",
        "objectives": [
            "Understand what a micro-interaction is",
            "Animate a loader or toggle switch",
            "Smooth out page transitions",
        ],
        "takeaways": [
            "Micro-interactions make the user experience feel alive",
            "Animations shouldn't be too long (150–300ms is ideal)",
            "Easing (ease-in-out) makes motion feel natural",
        ],
    },
    14: {
        "title": "Responsive Layouts",
        "description": "Designing for Mobile, Tablet, and Desktop screens.",
        "time": "16 min",
        "intro": "Use constraints, Auto Layout wrapping, and breakpoints to design screens that adapt across Mobile, Tablet, and Desktop.",
        "objectives": [
            "Use constraints (pin left/right/top/bottom)",
            "Define breakpoints for different screen sizes",
            "Adapt a layout for both mobile and desktop",
        ],
        "takeaways": [
            "Constraints define how an element behaves when resized",
            "Designing mobile-first is usually easier",
            "Auto Layout wrapping helps build responsive layouts",
        ],
    },
    15: {
        "title": "Final Portfolio Project",
        "description": "Creating a complete real-world mobile app UI design.",
        "time": "30+ min",
        "intro": "Combine everything you've learned to design a complete, multi-screen mobile app UI — ready for your portfolio.",
        "objectives": [
            "Apply everything you've learned in one project",
            "Go from idea to interactive prototype",
            "Prepare the project for your portfolio",
        ],
        "takeaways": [
            "A portfolio project is the best way to show your skills to employers",
            "Getting regular feedback improves the final result",
            "Even a small project, if finished well, has real value",
        ],
    },
}
 
 
# ---------------------------------------------------------
# App routes
# ---------------------------------------------------------
@app.route("/dashboard")
@login_required
def dashboard():
    lessons = [
        {"id": lid, "title": l["title"], "description": l["description"]}
        for lid, l in LESSONS.items()
    ]
    return render_template(
        "dashboard.html", lessons=lessons, user_name=session["user_name"]
    )
 
 
@app.route("/lesson/<int:lesson_id>")
@login_required
def lesson(lesson_id):
    selected_lesson = LESSONS.get(lesson_id)
    if not selected_lesson:
        return redirect(url_for("dashboard"))
    return render_template("lesson.html", lesson=selected_lesson)
 
 
# ---------------------------------------------------------
# Admin-only route — only ADMIN_USERNAME can view registered users
# ---------------------------------------------------------
@app.route("/users")
@admin_required
def show_users():
    users_list = User.query.order_by(User.id.desc()).all()
    return render_template("users.html", users=users_list)
 
 
if __name__ == "__main__":
    app.run(debug=True)
 