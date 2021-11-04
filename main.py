from flask import Flask, render_template

app = Flask(__name__)

valstis = [
    ["Krētas sala", "Lorem ipsum sdfdsf sdfsdf sdfsdf sdfsdf"],
    ["Spānija", "Lorem ipsum sdfdsf sdfsdf sdfsdf sdfsdf"],
    ["Grieķija", "Lorem ipsum sdfdsf sdfsdf sdfsdf sdfsdf"],
    ["Bulgārija", "Lorem ipsum sdfdsf sdfsdf sdfsdf sdfsdf"],
]

@app.route("/")
def splashpage():
    return render_template('splash.html')

@app.route("/piedzivojums")
def homepage():
    return render_template('piedzivojums.html', valstis=valstis)