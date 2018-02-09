from __future__ import print_function
from controllers.PageController import PageController
from controllers.EmployeeController import EmployeeController
from index import app
import sys
from models.Employee import Employee
from flask_login import logout_user

@app.route('/')
def index():
    return PageController().index()

@app.route('/calendar')
def calendar():
    return EmployeeController().get()


from flask import Flask,session, request, flash, url_for, redirect, render_template, abort ,g
from flask.ext.login import login_user , logout_user , current_user , login_required

@app.route('/login', methods=['POST'])
def login():
   return EmployeeController().login()

@app.route('/logout')
def logout():
   return EmployeeController().logout()
