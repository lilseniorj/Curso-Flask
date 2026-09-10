import os
from datetime import datetime

from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


DB_FILE_PATH = os.path.join(
    os.path.dirname(__file__),
    "notes.sqlite"
)

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_FILE_PATH}"

app.config.setdefault("SQLALCHEMY_TRACK_MODIFICATIONS", False)


db = SQLAlchemy(app)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    create_at = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f"<Note {self.id}: {self.title}>"


@app.route("/")
def home():
    role = "normal"
    notes = ["Note 1", "Note 2", "Note 3"]
    return render_template("home.html", role=role, notes=notes)

@app.route("/about")
def about():
    return "This is a Notes app"


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        return "Form submitted successfully.", 201
    return "Contact page"

@app.route("/api/info")
def api_info():
    data = {
        "nombre": "Notes App",
        "version": "1.1.1"
    }
    return jsonify(data)


@app.route("/confirmation")
def confirmation():
    note = request.args.get("note")
    return render_template("confirmation.html", note=note)

@app.route("/create-note", methods=["GET", "POST"])
def create_note():
    if request.method == "POST":
        note = request.form.get("note", "Not found")
        return redirect(
            url_for("confirmation", note=note)
        )
    return render_template("note_form.html")