from flask_app import app
from flask_app.models.deck import Deck
from flask_app.models.monster import Monster
from flask import render_template, request, redirect, session


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/duel")
def duel():
    return render_template("duel.html")


@app.route("/duel/<int:id>")
def show_monster(id):
    one_monster = Monster.get_by_id(id)
    return redirect("/duel", one_monster=one_monster)
