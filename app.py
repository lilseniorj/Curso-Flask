from datetime import datetime

from flask import Flask, redirect, render_template, request, url_for

from config import Config
from models import Note, db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


@app.route("/")
def home():
    notes = Note.query.all()
    return render_template("home.html", notes=notes, now=datetime.now())


@app.route("/about")
def about():
    return "This is a Notes app"


@app.route("/create-note", methods=["GET", "POST"])
def create_note():
    if request.method == "POST":
        title = request.form.get("title", "")
        content = request.form.get("content", "")
        published_at = request.form.get("published_at", "")

        if published_at:
            published_at = datetime.fromisoformat(published_at)
        else:
            published_at = None

        note_db = Note(title=title, content=content, published_at=published_at)

        db.session.add(note_db)
        db.session.commit()

        return redirect(url_for("home"))
    return render_template("note_form.html")


@app.route("/edit-note/<int:note_id>", methods=["GET", "POST"])
def edit_note(note_id):
    note = Note.query.get_or_404(note_id)

    if request.method == "POST":
        title = request.form.get("title", "")
        content = request.form.get("content", "")
        published_at = request.form.get("published_at", "")
        if published_at:
            published_at = datetime.fromisoformat(published_at)
        else:
            published_at = None

        note.title = title
        note.content = content
        note.published_at = published_at

        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit_note.html", note=note)


@app.route("/delete-note/<int:note_id>", methods=["POST"])
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for("home"))
