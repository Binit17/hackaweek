import os
import psycopg2
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

def get_db_connection():
    conn= psycopg2.connect(
        host='localhost',
        database='sambad',
        user='hero',
        password='hero')
    
    return conn

@app.route('/')
def my_app():
    return render_template('index.html')

@app.route('/patient-dashboard')
def dashboard1():
    return render_template('patient-dashboard.html')

@app.route('/doctor-dashboard')
def dashboard2():
    return render_template('doctor-dashboard.html')

@app.route('/login')
def login():
    return render_template('pages-login.html')

@app.route('/finddoctor')
def finddoctors():
    conn=get_db_connection()
    cur=conn.cursor()
    cur.execute("SELECT * FROM doctor WHERE location = 'jhapa' ;")
    doctor= cur.fetchall()
    cur.close()
    conn.close()
    return render_template('finddoctors.html',doctor=doctor)

app.run(debug="True",port='4010')