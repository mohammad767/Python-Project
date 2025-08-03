import mysql.connector
import oop
import hashlib
from colorama import init, Fore, Style
import data
from datetime import datetime, timedelta,time
import random

def get_connection():
    return mysql.connector.connect(
        user="root",
        password="P@ssw0rd",
        host="127.0.0.1",
        port="3306",
        database="reserve"
    )
    
def create_acc_p():
    con = get_connection()
    cur = con.cursor()
    pation = oop.Pation()
    pation.name = input("Enter your name : ")
    while pation.name == "Noname" :
        print("Wrong")
        pation.name = input("Enter your name again : ")
    pation.family = input("Enter your family : ")
    while pation.family == "Nofamily" :
        print("wrong")
        pation.family = input("Enter your family again : ")
    pation.phonenumber = input("Enter your phone number : ")
    while pation.phonenumber == "000" :
        print("Wrong")
        pation.phonenumber =  input("Enter your phone number again : ")
    pation.gender = input("Enter your gender : ")
    while pation.gender == "____" :
        print("Wrong")
        pation.gender = input("Enter your gender again : ")
    pation.birth_date = input("Enter your birth date(DD/MM/YY) : ")
    while pation.birth_date == "00/00/00":
        print("Wrong")
        pation.birth_date = input("Enter your birth date again(DD/MM/YY) : ")
    pation.mcode = input("Enter your meli code : ")
    while pation.mcode == "____":
        print("Wrong")
        pation.mcode = input("Enter your meli code again : ")
    ch = input("Do you want have a username(Y/N) if you choose n usernaem = fullname : ")
    if ch.lower() == "n" :
        pation.username = pation.name+pation.family    
    else :
        pation.username = input("Enter your username : ") 
        while pation.username == "User" :
            print("Wrong")
            pation.username = input("Enter your username again : ")
    password = pation._password
    password = hashlib.sha256(password.encode())
    password = password.hexdigest()
    
    data = (
        pation._id,pation.name.title(),pation.family.title(),
        pation.phonenumber,pation.birth_date,
        pation.mcode,pation.gender,pation.username,password)
   
    sql = """INSERT INTO pation(p_id,name,family,phonenumber,birth_date, meli_code,gender,
    usernmae,password)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    cur.execute(sql,data)
    con.commit()
    print("Data add")
    print(pation.username)
    print(pation._password)
       
def create_acc_d():
    con = get_connection()
    cur = con.cursor()
    doc = oop.Doctor()
    doc.name = input("Enter your name : ")
    while doc.name == "Noname" :
        print("Wrong")
        doc.name = input("Enter your name again : ")
    doc.family = input("Enter your family : ")
    while doc.family == "Nofamily" :
        print("wrong")
        doc.family = input("Enter your family again : ")
    doc.phonenumber = input("Enter your phone number : ")
    while doc.phonenumber == "000" :
        print("Wrong")
        doc.phonenumber =  input("Enter your phone number again : ")
    doc.email = input("Enter your email : ")
    while doc.email == "noemail" :
        print("Wrong")
        doc.email = input("Enter your email again : ")
    doc.gender = input("Enter your gender : ")
    while doc.gender == "____" :
        print("Wrong")
        doc.gender = input("Enter your gender again : ")
    doc.birth_date = input("Enter your birth date(DD/MM/YY) : ")
    while doc.birth_date == "00/00/00":
        print("Wrong")
        doc.birth_date = input("Enter your birth date again(DD/MM/YY) : ")
    doc.mcode = input("Enter your meli code : ")
    while doc.mcode == "____":
        print("Wrong")
        doc.mcode = input("Enter your meli code again : ")
    print(data.degree)
    doc.degree = input("Enter your degree : ")
    while doc.degree == "____" :
        print("Wrong")
        doc.degree = input("Enter your degree again : ")
    print(data.specialties)
    doc.specialty = input("Enter your specialty : ")
    while doc.specialty == "____" :
        print("Wrong")
        doc.specialty = input("Enter your specialty again : ")
    doc.exp_year = input("Enter your expreinc year : ")
    while doc.exp_year == "0" :
        print("Wrong")
        doc.exp_year = input("Enter your expreinc year again : ")
    doc.medical_code = input("Enter your medical code : ")
    while doc.medical_code == "0" :
        print("Wrong")
        doc.medical_code = input("Enter your medical code again : ")
    doc.shift_hours = input("Enter your shift hours(01:00-24:00) : ")
    while doc.shift_hours == "0-0":
        print("Wrong")
        doc.shift_hours = input("Enter your shift hours again (01:00-24:00) : ")
    doc.__visit_cost = input("Enter your visit cost : ")
    while doc.__visit_cost == "00":
        print("Wrong")
        doc.__visit_cost = input("Enter your visit cost again : ")
    ch = input("Do you want have a username(Y/N) if you choose n usernaem = fullname : ")
    if ch.lower() == "n" :
        doc.username = doc.name+doc.family    
    else :
        doc.username = input("Enter your username : ") 
        while doc.username == "User" :
            print("Wrong")
            doc.username = input("Enter your username again : ")
    password = doc._password
    password = hashlib.sha256(password.encode())
    password = password.hexdigest()
    doc_data = (doc._id,doc.name,doc.family,doc.phonenumber,doc.email,
                doc.birth_date,doc.mcode,doc.gender,doc.specialty,doc.degree,
                doc.exp_year,doc.medical_code,doc.shift_hours,doc.__visit_cost,
                doc.username,password)
    sql = """INSERT INTO doctor(d_id,name,family,phonenumber,email,
    birth_date,meli_code,gender,specialty,degree,experience_years,medical_code,
    shift_hours,visit_cost,usernmae,password)VALUES(%s,%s,%s,%s,
    %s,%s,%s,%s,
    %s,%s,%s,%s,
    %s,%s,%s,%s)"""
    cur.execute(sql,doc_data)
    con.commit()
    print("data add")
    print(doc.username)
    print(doc._password)
    
def login_p():
    con = get_connection()
    cur = con.cursor()
    username = input("Enter your usernmae : ")
    password = input("Enter your password : ")
    password = hashlib.sha256(password.encode())
    cur.execute("SELECT p_id FROM pation WHERE usernmae = %s AND password = %s",
                (username, password.hexdigest()))
    result = cur.fetchone()[0]
    ok = False
    if result == None:
             print(Fore.RED + "Not found try again ⚠️")
    else:
        ok = True
    if ok :
        while True :
            print("a --> add visit")
            print("s --> search doctor")
            print("v --> see visits")
            print("x --> exit")
            ch = input("Enter your choice : ").lower()
            if ch == "a":
                add_visit(result)
            elif ch == "s" :
                search()
            elif ch == "v" :
                see_visits(result)
            elif ch == "x" : 
                print("Goodbye")
                break
            else :
                print("Invalid input")

def login_d():
    con = get_connection()
    cur = con.cursor()
    username = input("Enter your usernmae : ")
    password = input("Enter your password : ")
    password = hashlib.sha256(password.encode())
    cur.execute("SELECT d_id FROM doctor WHERE usernmae = %s AND password = %s",
                (username, password.hexdigest()))
    result = cur.fetchone()[0]
    ok = False
    if result == None:
             print(Fore.RED + "Not found try again ⚠️")
    else:
        ok = True
    if ok :
        update(result)
        day_visit(result)
        
def get_docs() :
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT d_id,name,family,specialty,visit_cost FROM doctor")
    doc_lst = cur.fetchall()
    cur.execute("SELECT d_id FROM doctor")
    id_lst = [row[0] for row in cur.fetchall()]
    for i in  range(len(doc_lst)) : 
        print(f"doctor id : {doc_lst[i][0]}  doctor name : {doc_lst[i][1]} {doc_lst[i][2]}  specialty : {doc_lst[i][3]} visit cost : {doc_lst[i][4]} ")
        print("-"*20)
    id = int(input("Enter the doctor id : "))
    while id not in id_lst :
        print("Wrong")
        id = int(input("Enter the doctor id : "))
    
    return id    

def add_visit(id):
    con = get_connection()
    cur = con.cursor()
    vis = oop.visit()
    vis._id = random.randint(1000,10000)
    vis.pation_id = id
    vis.doctor_id = get_docs()
    print(vis.doctor_id)
    cur.execute("SELECT visit_id FROM visit WHERE pation_id = %s AND doctor_id = %s AND status = %s",(id,vis.doctor_id,"Not check"))
    check = cur.fetchall()
    if not check :
        vis._date = datetime.now().date() + timedelta(days=2)
        cur.execute("SELECT shift_hours FROM doctor WHERE d_id = %s",(vis.doctor_id,))
        shift = cur.fetchone()[0]
        start = shift[0:2]
        end = shift[6:8]
        if start.startswith == "0" :
            start = start.lstrip("0")
        if end.startswith == "0" : 
            end = end.lstrip("0") 
        
        visit_hour = random.randint(int(start),int(end))
        visit_min = random.randint(0,59)
        vis._time = time(visit_hour,visit_min,0)
        
        cur.execute("SELECT visit_cost FROM doctor WHERE d_id = %s",(vis.doctor_id,))
        vis.cost = cur.fetchone()[0]
        cur.execute("SELECT MAX(number) FROM visit WHERE doctor_id = %s",(vis.doctor_id,))
        number = cur.fetchone()[0]
        if number == None :
            vis._number = 1
        else :
            vis._number = vis._number + number
        
        print(f"number :{vis._number}")
        vis_data = (vis._id,vis.pation_id,vis.doctor_id,vis._date,
                    vis._time,vis.cost,vis._number,vis._status)
        sql = """INSERT INTO visit(visit_id,pation_id,doctor_id,
        date,time,visit_cost,number,status)VALUES(%s,%s,%s,%s,
        %s,%s,%s,%s)"""
        cur.execute(sql,vis_data)
        con.commit()
        print("DATA ADD")
        return
    else :
        print("You have already have not check visit with this doctor")
        return

def search():
    con = get_connection()
    cur = con.cursor()
    fil = input("Search doctor by name,specialty : ")
    if fil.lower() == "name" :
        name = input("Enter doctor name : ").title()
        cur.execute("SELECT d_id,name,family,specialty,visit_cost FROM doctor WHERE name = %s",(name,))
        doc_lst = cur.fetchall()
        if doc_lst == None :
            print("Not found")
            return
        for i in  range(len(doc_lst)) : 
            print(f"doctor id : {doc_lst[i][0]}  doctor name : {doc_lst[i][1]} {doc_lst[i][2]}  specialty : {doc_lst[i][3]} visit cost : {doc_lst[i][4]} ")
            print("-"*20)
        return
    elif fil.lower() == "specialty" :
        spec = input("Enter the specialty : ")
        cur.execute("SELECT d_id,name,family,specialty,visit_cost FROM doctor WHERE specialty = %s",(spec,))
        doc_lst = cur.fetchall()
        if doc_lst == None :
            print("Not found")
            return
        else :
            for i in  range(len(doc_lst)) : 
                print(f"doctor id : {doc_lst[i][0]}  doctor name : {doc_lst[i][1]} {doc_lst[i][2]}  specialty : {doc_lst[i][3]} visit cost : {doc_lst[i][4]} ")
                print("-"*20)
                return
        
def doc_name(d_id):
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT name,family FROM doctor WHERE d_id = %s",(d_id,))
    data = cur.fetchone()
    fullname = f"{data[0]} {data[1]}"
    return fullname

def see_visits(id) :
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT doctor_id,date,time FROM visit WHERE pation_id = %s AND status = %s",(id,"Not check"))
    data = cur.fetchall()
    for index,value in enumerate(data,start=1):
        print(f"{index} - doctor name : {doc_name(value[0])} date : {value[1]} time : {value[2]}")
        print("*"*20)
        
def day_visit(d_id):
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT date,time FROM visit WHERE doctor_id = %s AND status = %s",(d_id,"Not check"))
    d_data = cur.fetchall()
    for index,value in enumerate(d_data,start=1) :
        today = datetime.now().date()        
        if today.strftime("%d") == value[0].strftime("%d") :
            print(f"{index}-- {value[0]} {value[1]}")
            print("*"*10)
    if index == 1 :
        print("NO visit for today")   
         
def update(d_id) :
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT date,visit_id FROM visit WHERE doctor_id = %s AND status = %s",(d_id,"Not check"))
    d_data = cur.fetchall()
    today = datetime.now().date()
    for row in d_data :
        visit_date = row[0]
        visit_id = row[1] 
        if visit_date < today:
            cur.execute("UPDATE visit SET status = %s WHERE visit_id = %s", ("Expired", visit_id))
            con.commit()
# create table
def Pation():
    con = get_connection()
    cur = con.cursor()
    cur.execute("""CREATE TABLE pation(
        p_id INT primary key,
        name VARCHAR(15) not null,
        family VARCHAR(15) not null,
        phonenumber VARCHAR(11) unique,
        email VARCHAR(25) not null,
        birth_date VARCHAR(8) not null,
        meli_code VARCHAR(10),
        gender VARCHAR(6) not null,
        usernmae VARCHAR(20) not null,
        password VARCHAR(50) not null)""")
    print("Table create")

def Doctor():
    con = get_connection()
    cur = con.cursor()
    cur.execute("""CREATE TABLE doctor(
        d_id INT primary key,
        name VARCHAR(15) not null,
        family VARCHAR(15) not null,
        phonenumber VARCHAR(11) unique,
        email VARCHAR(25) not null,
        birth_date VARCHAR(8) not null,
        meli_code VARCHAR(10),
        gender VARCHAR(6) not null,
        specialty VARCHAR(30) unique,
        degree VARCHAR(10) not null,
        experience_years INT(2) not null,
        medical_code VARCHAR(10) not null,
        shift_hours VARCHAR(11) not null,
        visit_cost INT(5) not null,
        usernmae VARCHAR(20) not null,
        password VARCHAR(50) not null)""")
    print("Table create")

def visit():
    con = get_connection()
    cur = con.cursor()
    cur.execute("""CREATE TABLE visit(
        visit_id INT primary key,
        pation_id INT not null,
        doctor_id INT not null,
        date DATE not null,
        time TIME not null,
        visit_cost INT not null,
        number INT not null,
        status VARCHAR(15) not null,
        foreign key(pation_id)  references pation(p_id),
        foreign key(doctor_id)  references doctor(d_id)
        )""")    
    print("Table created")
