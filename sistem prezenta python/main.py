from flask import Flask, render_template, request
from datetime import date
import json
app = Flask(__name__)

members = []
today = date.today()


f = open("members.txt", "r")
g = open(str(today) + ".txt", "a")


for line in f:
    members.append(line)

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        global today
        global g
        option = request.form['options']
        if today != date.today():
            g.close()
            g = open(str(today) + ".txt", "a")
            today = date.today()
        print(option)
        g.write(str(option)+"\n")
    return render_template("index.html", members = members)




if __name__ == "__main__":
    app.run()