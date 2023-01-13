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
def homebeforelogin():
    return render_template('homebeforelogin.html')

@app.route('/home')
def homeafterlogin():
    return render_template('homeafterlogin.html')

@app.route('/patient-dashboard')
def patientProfile():
    return render_template('patient-dashboard.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/doctor')  #this is to send the appointment list to the doctor's profile.
def doctor():
    conn=get_db_connection()
    cur=conn.cursor()
    cur.execute("SELECT * FROM patient ;")
    patient = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('docprofile.html',patient = patient)

@app.route('/finddoctors',methods=('GET','POST'))
def finddoctors():
    if request.method == 'POST':
        #this is for filtering doctor
        location = 'kathmandu'
        location=request.form['location']
        conn=get_db_connection()
        cur=conn.cursor()
        cur.execute("SELECT * FROM doctor WHERE location= '%s';"%location)
        doc= cur.fetchall()
        cur.close()
        conn.close()
        return render_template('doctor-profile1.html',doc=doc)
    
    conn=get_db_connection()
    cur=conn.cursor()    
    cur.execute("SELECT * FROM doctor;")
    doc=cur.fetchall()
    cur.close()
    conn.close()
    return render_template('doctor-profile1.html',doc=doc)

@app.route('/appoint', methods=('GET','POST'))
def appointment():
    if request.method == 'POST':
        #this is for appointment
        email=request.form['email']
        address=request.form['address']
        age=int(request.form['age'])
        phone=request.form['phone']
        fullname=request.form['fullname']
        
        conn=get_db_connection()
        cur=conn.cursor()

        cur.execute('INSERT INTO patient(name,age,phone,location,email)'
                    'VALUES (%s,%s,%s,%s,%s)',
                    (fullname,age,phone,address,email))
        
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('patientProfile'))


    return render_template('appointment-form.html')

app.run(debug=True,port=9696)