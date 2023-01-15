from flask import Flask, url_for, render_template, request, session, redirect
from flaskext.mysql import MySQL
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)

# sql config
app.config['MYSQL_DATABASE_USER'] = os.getenv('MYSQL_DATABASE_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_DATABASE_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.getenv('MYSQL_DATABASE_DB')
app.config['MYSQL_DATABASE_HOST'] = os.getenv('MYSQL_DATABASE_HOST')
mysql = MySQL(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    # Get the user input
    username = request.form['username']
    password = request.form['password']

    # Create a cursor
    cursor = mysql.get_db().cursor()

    # Get the user by username
    cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
    user = cursor.fetchone()

    # If the user exists and the password is correct
    if user and user['password'] == password:
        # Create a session for the user
        session['username'] = user['username']
        return redirect('/dashboard')
    else:
        return 'Invalid username/password'


@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
