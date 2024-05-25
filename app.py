from flask import Flask, render_template, request
from secrets import token_urlsafe

app = Flask(__name__)
DEBUG = True
@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        userInput = request.form.get("userInput")
        userInput = int(userInput)-1
        randompass = token_urlsafe( userInput )
        return render_template("result.html", data = randompass)
@app.route("/about")
def about():
    return render_template("about.html")


app.run(port=80,debug=True)

