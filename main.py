from flask import Flask, render_template, request
import json

app = Flask(__name__)



@app.route("/")
def home():

    referrer = request.referrer


    if referrer != None:
        if "adityanambidi" not in referrer and "repl" not in referrer: 
            rp = open("t/links.txt", "r").read()

            refs = rp + '\n' + referrer

            open("t/links.txt", "w").write(refs)

            NUMV = open("t/numv.txt", "r").read()
            
            NUMV = int(NUMV)
            NUMV += 1

            open("t/numv.txt", "w").write(str(NUMV))

    projs = []

    with open("projects.json") as f:
        projs = json.loads(f.read())

    return render_template("index.html", projects=projs)


def create_app():
    return app