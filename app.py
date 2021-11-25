from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/java-info")
def javaInfo():
    return render_template("java-info.html")

@app.route("/python-info")
def pythonInfo():
    return render_template("python-info.html")