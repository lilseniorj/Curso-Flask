from functools import wraps

from flask import flash, redirect, session, url_for


def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if "user" not in session:
            flash("You most log in to access this page,", "error")
            return redirect(url_for("auth.login"))
        return view(*args, **kwargs)

    return wrapped_view