from flask import Blueprint, render_template, request, flash, redirect, url_for
from datetime import datetime

main = Blueprint('main', __name__)

visit_count = 0

@main.route("/", methods=["GET", "POST"])
def index():
    global visit_count
    visit_count += 1

    return render_template(
        "index.html",
        date=datetime.now().strftime("%d %B %Y"),
        time=datetime.now().strftime("%H:%M:%S"),
        visits=visit_count
    )
