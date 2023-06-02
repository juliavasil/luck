from flask import render_template, url_for


def index_page():
    return render_template("index.html")


