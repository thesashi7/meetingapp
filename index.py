from flask import Flask, redirect
from flask_login import LoginManager
from models.Employee import Employee
from config.config import Config
from utils.LogIn import LogIn

app = Flask(__name__)
app.config.update(dict(
        SECRET_KEY=Config.SECRET_KEY,
        WTF_CSRF_SECRET_KEY=Config.WTF_CSRF_SECRET_KEY
))

LogIn.employee_login(app)

if __name__ == '__main__':
    from routes import *

    app.run(debug=True)
