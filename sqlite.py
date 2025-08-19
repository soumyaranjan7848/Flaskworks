from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

def init_db():
    with sql.connect("database.db") as con:
        con.execute('''
            CREATE TABLE IF NOT EXISTS student (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                addr TEXT NOT NULL,
                city TEXT NOT NULL,
                pin TEXT NOT NULL
            )
        ''')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enternew')
def new_student():
    return render_template('student.html')

@app.route('/addrec', methods=['POST'])
def addrec():
    try:
        nm = request.form['nm']
        addr = request.form['add']
        city = request.form['city']
        pin = request.form['pin']

        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO student (name,addr,city,pin) VALUES (?,?,?,?)", 
                        (nm, addr, city, pin))
            con.commit()
            msg = "Record successfully added"
    except sql.Error as e:
        msg = f"Error in insert operation: {e}"

    return render_template("result.html", msg=msg)

@app.route('/list')
def list_students():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    con.close()
    return render_template("list.html", rows=rows)

if __name__ == '__main__':
    init_db()  # Ensure table exists before running
    app.run(debug=True)
