from dotenv import load_dotenv
from flask import Flask
from flaskext.mysql import MySQL
from flask_session import Session
from flask_bcrypt import Bcrypt
from flask_cors import CORS

import os
import views

load_dotenv()


def login_endpoint_handler_factory(app):
    def login_endpoint_handler():
        return views.login(app)

    return login_endpoint_handler


def register_endpoint_handler_factory(app):
    def register_endpoint_handler():
        return views.register(app)

    return register_endpoint_handler


app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = os.getenv('MYSQL_DATABASE_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_DATABASE_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.getenv('MYSQL_DATABASE_DB')
app.config['MYSQL_DATABASE_HOST'] = os.getenv('MYSQL_DATABASE_HOST')
mysql.init_app(app)
app.mysql = mysql
print('connected to db: ' + os.getenv('MYSQL_DATABASE_DB'))

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
print('session started')

CORS(app)

bcrypt = Bcrypt(app)
app.bcrypt = bcrypt
app.add_url_rule('/login', 'login', login_endpoint_handler_factory(app), methods=['POST'])
# app.add_url_rule('/login', methods=['POST'], view_func=views.login)
app.add_url_rule('/login', methods=['GET'], view_func=views.login_page)
# app.add_url_rule('/register', methods=['POST'], view_func=views.register)
app.add_url_rule('/register', 'register', register_endpoint_handler_factory(app), methods=['POST'])
app.add_url_rule('/logout', view_func=views.logout)
app.add_url_rule('/', view_func=views.home)

if __name__ == '__main__':
    app.run(debug=True)
