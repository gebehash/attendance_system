from flask import Flask, render_template, request
from datetime import date

app = Flask(__name__)
today = date.today()

members = []
checker = {}

f = open("members.txt", "r")
for line in f:
    members.append(line)
    line = line[:-1] if line[-1] == '\n' else line
    checker[str(line)] = 1

print(checker)

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        global today
        global g
        g = open(str(date.today()) + ".txt", "a")
        if checker[str(request.form['options'])] == 1:
            print(request.form['options'])
            g.write(str(request.form['options'])+" - ")
            g.write(request.form['descriere']+"\n\n")
            g.close()
            checker[str(request.form['options'])] == 0
    return render_template("index.html", members = members)


if __name__ == "__main__":
    app.run(port = 80, host = '0.0.0.0')