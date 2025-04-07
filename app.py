from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Create the database table if it doesn't exist
def init_db():
    conn = sqlite3.connect('queries.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def contact_form():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_query():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    conn = sqlite3.connect('queries.db')
    c = conn.cursor()
    c.execute("INSERT INTO queries (name, email, message) VALUES (?, ?, ?)", (name, email, message))
    conn.commit()
    conn.close()

    return "Your query has been submitted. Thank you!"

if __name__ == '__main__':
    app.run(debug=True)
