from flask import Flask, render_template, request
import json
import sqlite3

app = Flask(__name__)
db = sqlite3.connect("E://Kods//Kods//Coursework2//web.db", check_same_thread=False)
cursor = db.cursor()


@app.route("/")
def about():
    return render_template("main.html")


@app.route("/perfomance")
def index():
    return render_template("perfomance.html")


@app.route("/get_evaluations", methods=['GET', 'POST'])
def get_evaluations():
    if request.method == 'POST':
        res = cursor.execute("SELECT * from student where id = ?", (json.loads(request.data)['id_student'],)).fetchone()
        db.commit()
        if res is not None:
            return json.dumps({'name': res[1], 'mathematics': res[2], 'russian language': res[3],
                               'literature': res[4], 'OBZH': res[5], 'biology': res[6]}), 200
        else:
            return json.dumps({'error': 'id not in db'}), 200
    else:
        return render_template("perfomance.html")


if __name__ == "__main__":
    app.run(debug=True)