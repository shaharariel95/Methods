from flask import render_template, request, session, redirect, g, current_app


def home():
    if not session.get("email"):
        # if not there in the session then redirect to the login page
        return redirect("/login")
    return render_template('home.html')


def login_page():
    return render_template('login.html')


def login():
    if request.form['email'] == 'admin@example.com':
        if request.form['password'] == 'admin':
            session["email"] = request.form.get("email")
            print("email: " + session['email'])
            return redirect('/')
        else:
            return login_page()
    else:
        return login_page()


def register():
    return render_template('register.html')
