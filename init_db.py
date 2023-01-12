import os
import psycopg2

conn=psycopg2.connect(
    host="localhost",
    database = "sambad",
    user="hero",
    password="hero")

cur=conn.cursor()

cur.execute('DROP TABLE IF EXISTS doctor;')
cur.execute('DROP TABLE IF EXISTS patient;')
cur.execute('DROP TABLE IF EXISTS report;')

cur.execute('CREATE TABLE doctor (doc_id SERIAL PRIMARY KEY,'
            'name varchar(50) NOT NULL,'
            'age int NOT NULL,'
            'gender varchar(10) NOT NULL,'
            'email varchar(50) NOT NULL ,'
            'phone_no varchar(20)NOT NULL ,'
            'NMC_no int NOT NULL ,'
            'qualification varchar(10) NOT NULL,'
            'location varchar(50) NOT NULL,'
            'hospital varchar(50) NOT NULL,'
            'blogs text);'
            )

cur.execute('CREATE TABLE patient (pat_id SERIAL PRIMARY KEY,'
            'name varchar(50) NOT NULL,'
            'age int NOT NULL,'
            'phone varchar(50) NOT NULL ,'
            'location varchar(50) NOT NULL,'
            'email varchar(50) NOT NULL);'
            )

cur.execute('INSERT INTO patient(name,age,phone,location,email)'
            'VALUES(%s,%s,%s,%s,%s)',
            ('hunnybunny',30,'9841149889','kathmandu','binit@gmail.com')
            )

cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Binit K.C.',30,'male','binit@gmail.com','9812345678','1234','MD','kathmandu','Gangalal hospital','aldihgaldbaidgbabglakdblakdblasdbgkabdglabdlabldsblas')
            )
cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Anil Paudel',40,'female','anilpaudel@gmail.com','9812345678','100','MBBS','pokhara','nepal hospital','aldihgaldbaidgbabglakdblakdblasdbgkabdglabdlabldsblas')
            )
cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr Agrim Paneru',50,'male','agrimpaneru@gmail.com','9812345678','200','MBBS','kathmandu','BNB hospital','aldihgaldbaidgbabglakdblakdblasdbgkabdglabdlabldsblas')
            )
cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Ashim Karki',60,'male','ashimkarki@gmail.com','9812345678','401','MD','birgunj','mula hospital','aldihgaldbaidgbabglakdblakdblasdbgkabdglabdlabldsblas')
            )
cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Bishal Aryal',70,'female','bishalaryal@gmail.com','9812345678','1234','MD','jhapa','Vega hospital','aldihgaldbaidgbabglakdblakdblasdbgkabdglabdlabldsblas')
            )

cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Shyam Kafle',43, 'female', 'shyam kafle@gmail.com', '9640979532', 186, 'MBBS', 'Pokhara', 'YZ Hospital','ljbljbji')
            )

cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Chandra Gautam',81, 'female', 'chandra gautam@gmail.com', '8714470434', 162, 'D.Litt', 'Jhapa', 'STU Medical Center','adfasdfasdfaf')
            )

cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr.Binit Thapa', 45, 'male', 'dr.binit thapa@gmail.com', '6892214738', 185, 'DNB', 'Bardiya', 'GHI Medical Center','adfasdfasdfaf'))

cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Lisa Bajracharya', 40, 'male', 'lisa bajracharya@gmail.com', '1006777087', 167, 'MBBS', 'Bardiya', 'YZ Hospital','adfasdfasdfaf'))

cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Chandra Gautam', 36, 'female', 'chandra gautam@gmail.com', '9286117678', 178, 'MD', 'Kathmandu', 'JKL Health Center','adfasdfasdfaf'))

cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Robert Karki', 79, 'female', 'robert karki@gmail.com', '3068183886', 175, 'D.Litt', 'Bardiya', 'ABC Hospital','adfasdfasdfaf'))

cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Prem Paudel', 81, 'female', 'prem paudel@gmail.com', '1128710587', 196, 'D.Litt', 'Bardiya', 'DEF Clinic','adfasdfasdfaf'))

cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Riwaz Basnet ', 72, 'male', 'riwaz basnet @gmail.com', '6153031591', 175, 'MS', 'Kathmandu', 'MNO Hospital','adfasdfasdfaf'))

cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
           ('Dr. Shyam Kafle', 59, 'male', 'shyam kafle@gmail.com', '3779405952', 156, 'M.Ch', 'Bardiya', 'VWX Health Center','adfasdfasdfaf'))

cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Man Singh', 30, 'male', 'man singh@gmail.com', '3819716228', 159, 'M.Ch', 'Bardiya', '123 Clinic','adfasdfasdfaf'))

cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Smrity Pandit',19,'female','smritypandit@gmail.com','9812345678','1234','MD','pokhara','Vega hospital','adfasdfasdfaf')
            )

conn.commit()
cur.close()
conn.close()

