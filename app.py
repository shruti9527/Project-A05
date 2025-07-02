from flask import Flask, render_template, request
import sqlite3
 
app = Flask(__name__)
 
# Initialize database
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
 
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/submit', methods=['GET','POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
 
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()
 
    return render_template('submit.html', name=name, email=email)
 
if __name__ == '__main__':
    init_db()
    app.run(debug=True)