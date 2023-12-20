from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/articles")
def articles():
    return render_template("articles.html")


if __name__ == '__main__':
    app.run(debug=True)
