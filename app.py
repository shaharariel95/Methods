from dotenv import load_dotenv
from flask import Flask, session
from flask_session import Session
import views

load_dotenv()


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.add_url_rule('/login', methods=['POST'], view_func=views.login)
app.add_url_rule('/login', methods=['GET'], view_func=views.login_page)
app.add_url_rule('/register', view_func=views.register)
app.add_url_rule('/', view_func=views.home)

if __name__ == '__main__':
    app.run(debug=True)
