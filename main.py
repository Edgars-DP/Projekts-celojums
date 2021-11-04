from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def splashpage():
    return render_template('splash.html')