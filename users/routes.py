from flask import Blueprint, render_template

users_bp = Blueprint("users", __name__)



@users_bp.route("/register")
def register():
    return render_template("register.html")
