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
            ('Anil Paudel',30,'9841149889','kathmandu','binit@gmail.com')
            )

cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Binit K.C.',30,'male','binit@gmail.com','9812345678',1234,'MD','kathmandu','Prasuti Griha','aldihgaldbaidgbabglakdblakdblasdbgkabdglabdlabldsblas')
            )
cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Anil Paudel',40,'male','anilpaudel@gmail.com','9812345678',6754,'MBBS','pokhara','Pokhara Hospital','aldihgaldbaidgbabglakdblakdblasdbgkabdglabdlabldsblas')
            )
cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr Agrim Paneru',50,'male','agrimpaneru@gmail.com','9812345678',200,'MBBS','kathmandu','Norvic Hospital','aldihgaldbaidgbabglakdblakdblasdbgkabdglabdlabldsblas')
            )
cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Ashim Karki',60,'male','ashimkarki@gmail.com','9812345678',101,'MD','bardiya','bardiya hospital','aldihgaldbaidgbabglakdblakdblasdbgkabdglabdlabldsblas')
            )
cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Agrim Paudel', 40, 'male', 'agrimpaudel@gmail.com', '9822822454', 197, 'MBBS', 'jhapa', 'Birta City Hospital', 'asjdkasjdksajd'))

cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Shyam Kafle',43, 'female', 'shyam kafle@gmail.com', '9640979532', 186, 'MBBS', 'pokhara', 'YZ Hospital','ljbljbji')
            )

cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Chandra Gautam',61, 'female', 'chandra gautam@gmail.com', '8714470434', 1562, 'MBBS/MD', 'jhapa', 'STU Medical Center','adfasdfasdfaf')
            )

cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr.Binit Thapa', 45, 'male', 'dr.binit thapa@gmail.com', '6892214738', 5185, 'DNB', 'bardiya', 'GHI Medical Center','adfasdfasdfaf'))

cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Lisa Bajracharya', 40, 'male', 'lisa bajracharya@gmail.com', '1006777087', 3167, 'MBBS', 'bardiya', 'YZ Hospital','adfasdfasdfaf'))

cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Chandra Gautam', 36, 'female', 'chandra gautam@gmail.com', '9286117678', 4178, 'MD', 'Kathmandu', 'JKL Health Center','adfasdfasdfaf'))

cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Robert Karki', 39, 'female', 'robert karki@gmail.com', '3068183886', 4175, 'MBBS/MD', 'bardiya', 'ABC Hospital','adfasdfasdfaf'))

cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Prem Paudel', 51, 'female', 'prem paudel@gmail.com', '1128710587', 1596, 'MBBS', 'bardiya', 'DEF Clinic','adfasdfasdfaf'))

cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Riwaz Basnet ', 72, 'male', 'riwaz basnet @gmail.com', '6153031591', 1575, 'MS', 'kathmandu', 'MNO Hospital','adfasdfasdfaf'))

cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
           ('Dr. Shyam Kafle', 59, 'male', 'shyam kafle@gmail.com', '3779405952', 1556, 'M.Ch', 'bardiya', 'VWX Health Center','adfasdfasdfaf'))

cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Man Singh', 30, 'male', 'man singh@gmail.com', '3819716228', 1579, 'M.Ch', 'bardiya', '123 Clinic','adfasdfasdfaf'))

cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Smrity Pandit',19,'female','smritypandit@gmail.com','9812345678','1234','MD','pokhara','Vega hospital','adfasdfasdfaf')
            )
cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Indra Prasad', 30, 'male', 'prasadindra@gmail.com', '3819716228', 1579, 'M.Ch', 'kathmandu', '123 Clinic','adfasdfasdfaf'))
cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Samana Pathak', 34, 'female', 'pathaksamana@outlook.com', '9821345231', 3452, 'MBBS/MD', 'jhapa', 'Oli clinic','dfgjsdfas'))
cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Laxmi Pun', 45, 'female', 'laxmipun@gmail.com', '9837912971', 1767, 'MDS', 'jhapa', 'B.P. Koirala Institute of Health Sciences', 'asjdkasjdksajd'))
cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Pooja Magar', 53, 'female', 'poojamagar@gmail.com', '9827251551', 195, 'MBBS', 'pokhara', 'Mediciti Hospital', 'asjdkasjdksajd'))
cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Sunita Shah ', 34, 'female', 'shahsunita@gmail.com', '9834212312',4452, 'MBBS/MD', 'pokhara', 'pokhara materntiy hopsital','dfgjsdfas'))
cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Aarati Sharma', 50, 'male', 'aaratisharma@gmail.com', '9831761002', 157, 'PhD', 'jhapa', 'Bir Hospital', 'asjdkasjdksajd'))
cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Anjali Adhikari', 37, 'female', 'anjaliadhikari@gmail.com', '9839382134', 168, 'MBBS', 'kathmandu', 'Bir Hospital', 'asjdkasjdksajd'))
cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Ganga Bhandari', 57, 'female', 'gangabhandari@gmail.com', '9818687027', 174, 'MS', 'bardiya', 'Lions Club Hospital', 'asjdkasjdksajd'))
cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Anjali Adhikari', 42, 'female', 'anjaliadhikari@gmail.com', '9821720157', 178, 'PhD', 'bardiya', 'Kathmandu Medical College', 'asjdkasjdksajd'))
cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Laxmi Pun', 52, 'female', 'laxmipun@gmail.com', '9824463537', 176, 'MS', 'Jhapa', 'kathmandu Model Hospital', 'asjdkasjdksajd'))
cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Aarati Sharma', 59, 'male', 'aaratisharma@gmail.com', '9829486867', 169, 'MD', 'kathmandu', 'Nepal Medical College', 'asjdkasjdksajd'))
cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Aasha Thapa', 60, 'female', 'aashathapa@gmail.com', '9819545558', 191, 'MDS', 'bardiya', 'Bir Hospital', 'asjdkasjdksajd'))
cur.execute('INSERT INTO doctor(name,age,gender,email,phone_no,NMC_no,qualification,location,hospital,blogs)'
            'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ('Dr. Anisha Thapa', 60, 'female', 'aashathapa@gmail.com', '9819545558', 191, 'MDS', 'bardiya', 'Bir Hospital', 'asjdkasjdksajd'))

conn.commit()
cur.close()
conn.close()