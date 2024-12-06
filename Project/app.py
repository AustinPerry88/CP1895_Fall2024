from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, NumberRange
import sqlite3

# Flask application setup
app = Flask(__name__)
app.secret_key = "secret-key"

db_path = "players.db"

# Database utility functions
def create_database():
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Player (
            playerID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            batOrder INTEGER NOT NULL,
            firstName TEXT NOT NULL,
            lastName TEXT NOT NULL,
            position TEXT NOT NULL,
            atBats INTEGER,
            hits INTEGER
        )
        ''')

def get_all_players():
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Player ORDER BY batOrder")
        return cursor.fetchall()

def add_player(bat_order, first_name, last_name, position, at_bats, hits):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Player (batOrder, firstName, lastName, position, atBats, hits) VALUES (?, ?, ?, ?, ?, ?)",
            (bat_order, first_name, last_name, position, at_bats, hits)
        )

def update_player(player_id, bat_order, first_name, last_name, position, at_bats, hits):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE Player
            SET batOrder = ?, firstName = ?, lastName = ?, position = ?, atBats = ?, hits = ?
            WHERE playerID = ?
            """,
            (bat_order, first_name, last_name, position, at_bats, hits, player_id)
        )

def delete_player(player_id):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Player WHERE playerID = ?", (player_id,))

# WTForms setup
class PlayerForm(FlaskForm):
    batOrder = IntegerField("Batting Order", validators=[DataRequired(), NumberRange(min=1)])
    firstName = StringField("First Name", validators=[DataRequired()])
    lastName = StringField("Last Name", validators=[DataRequired()])
    position = SelectField("Position", choices=["Pitcher", "Catcher", "First Base", "Second Base", "Shortstop", "Third Base", "Outfield"], validators=[DataRequired()])
    atBats = IntegerField("At Bats", validators=[NumberRange(min=0)])
    hits = IntegerField("Hits", validators=[NumberRange(min=0)])
    submit = SubmitField("Submit")

@app.route("/")
def index():
    players = get_all_players()
    return render_template("index.html", players=players)

@app.route("/add", methods=["GET", "POST"])
def add():
    form = PlayerForm()
    if form.validate_on_submit():
        add_player(form.batOrder.data, form.firstName.data, form.lastName.data, form.position.data, form.atBats.data or 0, form.hits.data or 0)
        flash("Player added successfully!", "success")
        return redirect(url_for("index"))
    return render_template("add.html", form=form)

@app.route("/edit/<int:player_id>", methods=["GET", "POST"])
def edit(player_id):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Player WHERE playerID = ?", (player_id,))
        player = cursor.fetchone()

    if not player:
        flash("Player not found!", "danger")
        return redirect(url_for("index"))

    form = PlayerForm()
    if request.method == "POST" and form.validate_on_submit():
        update_player(player_id, form.batOrder.data, form.firstName.data, form.lastName.data, form.position.data, form.atBats.data or 0, form.hits.data or 0)
        flash("Player updated successfully!", "success")
        return redirect(url_for("index"))

    form.batOrder.data, form.firstName.data, form.lastName.data, form.position.data, form.atBats.data, form.hits.data = player[1:]
    return render_template("edit.html", form=form)

@app.route("/delete/<int:player_id>", methods=["POST"])
def delete(player_id):
    delete_player(player_id)
    flash("Player deleted successfully!", "success")
    return redirect(url_for("index"))

if __name__ == "__main__":
    create_database()
    app.run(debug=True)
