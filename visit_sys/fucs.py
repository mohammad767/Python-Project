import mysql.connector




def get_connection():
    return mysql.connector.connect(
        user="root",
        password="P@ssw0rd",
        host="127.0.0.1",
        port="3306",
        database="reserve"
    )
    
    
    


#Create tabel

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
