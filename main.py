from flask import Flask, render_template
from db import *

app = Flask(__name__)

#valstis = [
#    ["Krētas sala", "Lorem ipsum sdfdsf sdfsdf sdfsdf sdfsdf"],
#    ["Spānija", "Lorem ipsum sdfdsf sdfsdf sdfsdf sdfsdf"],
#    ["Grieķija", "Lorem ipsum sdfdsf sdfsdf sdfsdf sdfsdf"],
#    ["Bulgārija", "Lorem ipsum sdfdsf sdfsdf sdfsdf sdfsdf"],
#]

print(db_exec("select * from valstis").fetchall())

@app.route("/")
def splashpage():
    return render_template('splash.html')

@app.route("/piedzivojums")
def homepage():
    return render_template('piedzivojums.html', valstis=db_exec("select * from valstis").fetchall())