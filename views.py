from flask import render_template, request, session, redirect, Response
import ezshop_algo_api as ez
import json


def home():
    predictedCart = {}
    oldCart = {}

    if not session.get("username"):
        # if not there in the session then redirect to the login page
        return redirect("/login")
    amount = ez.amount_of_lists(session['id'])
    if amount != 0:
        predictedCart = ez.predict_list(session['id'], 10)
        for keys in predictedCart:
            predictedCart[keys] = int(predictedCart[keys])
        oldCart = ez.get_last_list(session['id'])
        for keys in oldCart:
            oldCart[keys] = int(oldCart[keys])
    # print(oldCart)
    return render_template('index.html', predictedCart=predictedCart, oldCart=oldCart, amount=amount)


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
        session['id'] = user['id']
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


def get_num_of_lists():
    x = ez.amount_of_lists(session['id'])
    print(x)
    return redirect('/')


def add_cart():
    newCart = ez.get_empty_products_list()
    return render_template('newCart.html', newCart=newCart)


def add_cart_to_list():
    predictedCart = ez.predict_list(session['id'], 10)
    # predictedCart['time_from_last_buy'] = 10
    ez.add_list(session['id'], predictedCart)
    return Response(status=200)


def new_cart():
    newCart = request.form
    newCart = dict(newCart)
    newCart = {k: int(v) for k, v in newCart.items()}
    ez.add_list(session['id'], newCart)
    return redirect('/')


def edit_cart():
    predicted = ez.predict_list(session['id'], 10)
    for keys in predicted:
        predicted[keys] = int(predicted[keys])
    return render_template('editCart.html', predicted=predicted)
