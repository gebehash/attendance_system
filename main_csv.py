from flask import Flask, render_template, request
from datetime import date
import csv

#problema: nu se reseteaza checkerul de nume dupa ce se termina ziua DONE

#intra pe pagina verifica ziua, daca s-a terminat se reseteaza checkerul si se insereaza data in fisier
#dupa se pun in fisier optiunile alese/scrise SPER CA MERGE

app = Flask(__name__)
today = date.today()

csv_file = open(str(date.today()) + ".csv", 'a')
csv_reader = csv.reader(csv_file, delimiter=',')
csv_writer = csv.writer(csv_file, delimiter=',')

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
        global today, csv_file, date
        
        selected_name = str(request.form['options'])

        if today != date.today():
            for key in checker:
                checker[key] = 1
            today = date.today()
            
        csv_file = open(str(date.today()) + ".csv", 'a')
        csv_writer = csv.writer(csv_file, delimiter=',')

        if checker[selected_name] == 1:
            print(request.form['options'])
            items = [selected_name, request.form['descriere']]
            csv_writer.writerow(items)
            csv_file.close()
            checker[selected_name] = 0

    return render_template("index.html", members = members)


if __name__ == "__main__":
    app.run(port = 80, host = '0.0.0.0')