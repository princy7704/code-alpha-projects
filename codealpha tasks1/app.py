from flask import Flask, request, redirect, render_template
import sqlite3
import random
import string

app = Flask(__name__)

# Create database table
def init_db():
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_url TEXT NOT NULL,
            short_code TEXT NOT NULL UNIQUE
        )
    ''')

    conn.commit()
    conn.close()

# Generate random short code
def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Shorten URL
@app.route('/shorten', methods=['POST'])
def shorten_url():

    original_url = request.form['url']

    short_code = generate_short_code()

    conn = sqlite3.connect('urls.db')
    c = conn.cursor()

    c.execute(
        'INSERT INTO urls (original_url, short_code) VALUES (?, ?)',
        (original_url, short_code)
    )

    conn.commit()
    conn.close()

    short_url = request.host_url + short_code

    return render_template(
        'index.html',
        short_url=short_url
    )

# Redirect to original URL
@app.route('/<short_code>')
def redirect_url(short_code):

    conn = sqlite3.connect('urls.db')
    c = conn.cursor()

    c.execute(
        'SELECT original_url FROM urls WHERE short_code=?',
        (short_code,)
    )

    result = c.fetchone()

    conn.close()

    if result:
        return redirect(result[0])

    return "URL not found"

if __name__ == '__main__':
    init_db()
    app.run(debug=True)