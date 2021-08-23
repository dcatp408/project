from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/login_user", methods=["POST"])
def login_user():
    data = {"email": request.form["email"]}
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Account doesn't exist")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Account doesn't exist")
        return redirect("/")
    session['user_id'] = user_in_db.id
    return redirect("/dashboard")


@app.route("/register_user", methods=["POST"])
def register_user():
    if User.register_validate(request.form) == False:
        return redirect("/")
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "username": request.form["username"],
        "password": pw_hash,
    }
    user_id = User.save(data)
    session['user_id'] = user_id
    return redirect("/dashboard")


@app.route("/delete_session")
def delete_session():
    session.clear()
    return redirect("/")
