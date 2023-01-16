from dotenv import load_dotenv
from flask import Flask
from flaskext.mysql import MySQL
from flask_session import Session
from flask_bcrypt import Bcrypt

import os
import views

load_dotenv()

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = os.getenv('MYSQL_DATABASE_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_DATABASE_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.getenv('MYSQL_DATABASE_DB')
app.config['MYSQL_DATABASE_HOST'] = os.getenv('MYSQL_DATABASE_HOST')
mysql.init_app(app)
print('connected to db: ' + os.getenv('MYSQL_DATABASE_DB'))

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
print('session started')

bcrypt = Bcrypt(app)

app.add_url_rule('/login', methods=['POST'], view_func=views.login)
app.add_url_rule('/login', methods=['GET'], view_func=views.login_page)
app.add_url_rule('/register', methods=['POST'], view_func=views.register)
app.add_url_rule('/logout', view_func=views.logout)
app.add_url_rule('/', view_func=views.home)

if __name__ == '__main__':
    app.run(debug=True)
