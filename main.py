from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/blog")
def blog():
    return "<p>This is a blog</p>"

@app.route("/about")
def about():
    return render_template('about.html')
