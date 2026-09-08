from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    role = "normal"
    notes = ["Note 1", "Note 2", "Note 3"]
    return render_template("home.html", role=role, notes=notes)

@app.route("/about")
def about():
    return "This is a Notes app"


@app.route("/contact", methods=['GET', 'POST'])
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