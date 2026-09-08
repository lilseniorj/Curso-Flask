from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello lilseniorj!???!"

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
    return jsonify(data), 200