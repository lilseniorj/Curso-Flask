from flask import Blueprint, flash, redirect, render_template, request, session, url_for

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "")
        password = request.form.get("password", "")
        if email == "admin@admin.com" and password == "admin":
            session["user"] = email
            return redirect(url_for("notes.home"))
        flash("Invalid credentials", "error")
    return render_template("login.html")

@auth_bp.route("/logout", methods=["POST"])
def logout():
    session.pop("user", None)
    flash("You have been logged out", "success")
    return redirect(url_for("auth.login"))
