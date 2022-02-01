from flask import Flask, render_template, make_response, request, g
from random import randint
import sqlite3
import db
import json

app = Flask(__name__)

# valstis = [
#    ["Krētas sala", "Lorem ipsum sdfdsf sdfsdf sdfsdf sdfsdf"],
#    ["Spānija", "Lorem ipsum sdfdsf sdfsdf sdfsdf sdfsdf"],
#    ["Grieķija", "Lorem ipsum sdfdsf sdfsdf sdfsdf sdfsdf"],
#    ["Bulgārija", "Lorem ipsum sdfdsf sdfsdf sdfsdf sdfsdf"],
# ]

# Datubāze


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect("data.db")
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
# /Datubāze

# Pārbauda vai lietotājs ir administrators


def is_admin(req):
    print(req.cookies.get('admin_sesija'))
    if(
        get_db().cursor().execute(
            "SELECT * FROM admins WHERE sesija = ?;", 
            [req.cookies.get('admin_sesija')]
        ).fetchone() == None
    ):
        return False
    return True


@app.route("/")
def splashpage():
    return render_template('splash.html')


@app.route("/piedzivojums")
def homepage():
    return render_template(
        'piedzivojums.html', 
        valstis=get_db().cursor().execute("select * from valstis").fetchall()
    )

@app.route("/piedzivojums/<veids>")
def renderpiedzivojums(veids):
	piedzivojumi = ["Avio ceļojumi","Atpūtas ceļojumi","Kruīzi"]
	if veids in piedzivojumi:
		return render_template("ceļojumi.html", veids=veids)

@app.route("/rezervet")
def rezervet():
	return render_template("rezervet.html")


@app.route("/api/viesnicas/<valsts>")
def viesnicasvalsti(valsts):
	return json.dumps(
		get_db().execute("SELECT * FROM viesnicas WHERE valsts=?;", [valsts]).fetchall()
	)

@app.route("/api/viesnicas/<valsts>/cena/<viesnica>")
def viesnicascenasvalsti(valsts, viesnica):
	return json.dumps(
		get_db().execute("SELECT nakts FROM viesnicas WHERE valsts=? AND nosaukums=?;", [valsts, viesnica]).fetchall()
	)


# ============================================================================
# Pierakstās/izrakstās kā administrators

@app.route("/adm/login", methods=['POST', 'GET'])
def setadmin():
    resp = make_response(render_template(
        'redirToHome.html', 
        msg="Izdevās! Tu tagat esi administrators!"
    ))

    if(not(is_admin(request))):
        # Uzģenerē nejaušu skaitli
        session_cookie = randint(1111, 99999999)
        # Un ieliek to sīkdatnēs kā admintratora "paroli"
        get_db().cursor().execute("INSERT INTO admins VALUES (?)", [session_cookie])
        resp.set_cookie('admin_sesija', str(session_cookie))
        resp.set_data(render_template(
            'redirToHome.html',
            msg="Tu jau esi kā administrators!"
        ))

    return resp

@app.route("/adm/logout", methods=['POST', 'GET'])
def unsetadmin():
    resp = make_response(render_template(
        'redirToHome.html', 
        msg="Tu tiec izraktīts!"
    ))

    if(not(is_admin(request))):
        get_db().cursor().execute(
            "DELETE FROM admins WHERE sesija = ?;", 
            [request.cookies.get('admin_sesija')]
        )
        resp.set_cookie('admin_sesija', "0")

    return resp

@app.route("/adm", methods=['GET'])
def amiadmin():
    resp = make_response(render_template(
        'redirToHome.html', 
        msg=str(is_admin(request))
    ))
    return resp
