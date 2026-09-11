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
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f"Note {self.id}: {self.title}"


@app.route("/")
def home():
    notes = Note.query.all()
    return render_template("home.html", notes=notes)

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
        title = request.form.get("title", "")
        content = request.form.get("content", "")

        note_db = Note(
            title=title, content=content
        )

        db.session.add(note_db)
        db.session.commit()

        return redirect(
            url_for("home")
        )
    return render_template("note_form.html")