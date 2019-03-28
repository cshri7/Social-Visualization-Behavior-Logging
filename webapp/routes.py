from flask import render_template, flash, redirect, url_for, request
from flask_cors import CORS, cross_origin
from webapp import app
from webapp import db
from webapp.forms import LoginForm, RegistrationForm
from webapp.models import User, ActivityLog
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from datetime import datetime
import sqlite3

# comment
@app.route("/chart1")
def chart1():
    if current_user.username == "aaa":
        labels = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        values = [10,5,2,1,0,0,9]
    elif current_user.username == "bbb":
        labels = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        values = [0,9,4,7,3,0,0]
    elif current_user.username == "ccc":
        labels = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        values = [1,3,2,4,2,1,1]

    return render_template('chart1.html', values=values, labels=labels)

# mark favourite
@app.route("/chart2")
def chart2():
    if current_user.username == "aaa":
        labels = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        values = [10,6,0,0,1,0,8]
    elif current_user.username == "bbb":
        labels = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        values = [0,2,3,4,5,0,0]
    elif current_user.username == "ccc":
        labels = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        values = [2,1,1,2,1,0,3]

    return render_template('chart2.html', values=values, labels=labels)

# up vote
@app.route("/chart3")
def chart3():
    if current_user.username == "aaa":
        labels = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        values = [8,4,0,0,0,0,7]
    elif current_user.username == "bbb":
        labels = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        values = [0,7,6,5,4,0,0]
    elif current_user.username == "ccc":
        labels = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        values = [2,3,1,1,0,0,1]

    return render_template('chart3.html', values=values, labels=labels)

@app.route('/index', methods=['GET', 'POST'])
@login_required
@cross_origin()
def index():
    if request.method == "POST":
        data = request.form
        temp = dict(data)
        dict_data = {}
        for t in temp:
            dict_data[t] = temp[t][0]
        dict_data['count'] = int(dict_data['count'])
        query = ActivityLog(username=current_user.username, count=dict_data['count'], activity=dict_data['activity'], timestamp=['timestamp'])
        db.session.add(query)
        db.session.commit()
        print "inserted into db"
        return render_template('index.html', user=user, data=data)
    return render_template('index.html', title='Home Page')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('login'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/user/<username>', methods=['GET', 'POST'])
@login_required
def user(username):
    # print current_user
    user = User.query.filter_by(username=username).first_or_404()
    posts = ActivityLog.query.filter_by(username=username).first()
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    # print str(current_user.username)
    #c.execute("SELECT time, activity FROM ActivityLog WHERE username like '" + str(current_user.username) + "' ORDER BY id DESC LIMIT 20")
    # c.execute("INSERT INTO ACTIVITYLOG VALUES (1, 'aaa', 1, 'shared_posts', '9/20/2018, 4:03:31 AM')")
    # db.session.commit()
    # c.execute("SELECT * FROM ACTIVITYLOG")
    c.execute("SELECT * FROM USER")
    data = c.fetchall()
    # print "rendering"
    print data
    return render_template('user.html', user=user, data=data)

@app.before_request
def before_request():
    if current_user.is_authenticated:
        # current_user.last_seen = datetime.utcnow()
        current_user.last_login = datetime.utcnow()
        db.session.commit()
