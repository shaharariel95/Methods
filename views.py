from flask import render_template, request, session, redirect


def home():
    if not session.get("username"):
        # if not there in the session then redirect to the login page
        return redirect("/login")
    return render_template('home.html')


def login_page():
    return render_template('login.html')


def login(app):
    # Get the user input
    email = request.json['email']
    password = request.json['password']

    # Create a cursor
    conn = app.mysql.connect()
    cursor = conn.cursor()
    # cursor = app.mysql.get_db().cursor()

    # Get the user by username
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    result = cursor.fetchone()
    user = None
    if result:
        columns = [col[0] for col in cursor.description]
        user = dict(zip(columns, result))
    else:
        return {"reason": 'User was not found'}
    # If the user exists and the password is correct
    if user and app.bcrypt.check_password_hash(user['Password'], password):
        # Create a session for the user
        session['username'] = user['username']
        session['email'] = user['email']
        cursor.close()
        conn.close()
        return redirect('/')
    else:
        cursor.close()
        conn.close()
        return {"reason": 'Invalid password'}


def logout():
    session["email"] = None
    session["username"] = None
    return redirect("/")


def register(app):
    import app
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    pw_hashed = app.bcrypt.generate_password_hash(password, 10)
    conn = app.mysql.connect()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO `users` (`username`, `password`, `email`)"
                   " VALUES (%s, %s , %s)", (username, pw_hashed, email))
    conn.commit()

    cursor.close()
    conn.close()
    return redirect('/')
