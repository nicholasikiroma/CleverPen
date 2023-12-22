"""Base Flask Application for Blog"""
from flask import Flask, render_template, flash, url_for, request, redirect, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models.basemodel import db, Users, Posts
from flask_migrate import Migrate
from forms import SignUpForm, LoginForm, PostForm
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    current_user,
)
from flask_ckeditor import CKEditor
import openai
import os
from dotenv import load_dotenv

load_dotenv()


base_dir = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    base_dir, "cleverpen.db"
)
app.secret_key = os.getenv("SECRET_KEY")
openai.api_key = os.getenv("API_KEY")


db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
migrate = Migrate(app, db)
ckeditor = CKEditor(app)
login_manager.login_view = "login"


with app.app_context():
    db.create_all()


@app.login_manager.user_loader
def user_loader(id):
    """Handles user login"""
    return Users.query.get(int(id))


@app.route("/logout")
def log_out():
    logout_user()
    return redirect(url_for("index"))


@app.route("/")
def index():
    """Renders index page of blog"""
    author = current_user
    posts = Posts.query.order_by(Posts.date.desc())
    return render_template("index.html", posts=posts, author=author)


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    """Renders sign up form"""
    form = SignUpForm()
    if request.method == "POST" and form.validate_on_submit():
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        # checks if username exists in database
        check_username = Users.query.filter_by(username=username).first()
        if check_username:
            flash(f"{username} already exists....try something different.")
            return redirect(url_for("sign_up"))

        # checks if email address exists in database
        check_email = Users.query.filter_by(email=email).first()
        if check_email:
            flash(f"User with {email} already exists....try something different.")
            return redirect(url_for("sign_up"))

        password_hash = generate_password_hash(password)
        new_user = Users(username=username, email=email, password_hash=password_hash)

        db.session.add(new_user)
        db.session.commit()
        flash("Account created successfully!")
        return redirect(url_for("login"))

    return render_template("sign_up.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Renders sign up form"""
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        email = request.form.get("email")
        password = request.form.get("password")

        user_email = Users.query.filter_by(email=email).first()
        if user_email and check_password_hash(user_email.password_hash, password):
            login_user(user_email)
            return redirect(url_for("index"))
        else:
            flash("email/password Incorrect")
            return redirect(url_for("login"))

    return render_template("login.html", form=form)


@app.route("/writer", methods=["POST", "GET"])
@login_required
def writer():
    """Sends API request to OpenAI and saves edited content"""
    form = PostForm()

    if form.validate_on_submit():
        title = request.form.get("title")
        summary = request.form.get("summary")
        content = request.form.get("content")

        new_post = Posts(title=title, content=content, summary=summary)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("index"))

    return render_template("writer.html", form=form)


@app.route("/openai", methods=["POST"])
def generate_text():
    """Sends API request to OpenAI and returns"""
    request_data = request.get_json()
    text = request_data["text"]

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.7,
    )

    response_text = response["choices"][0]["text"]

    return jsonify({"response_text": response_text})


if __name__ == "__main__":
    app.run(debug=True)
