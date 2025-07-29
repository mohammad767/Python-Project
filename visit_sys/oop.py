import random
import string
import re
import datetime
import data
import mysql.connector

#random.randint()

con = mysql.connector.connect(
        user="root",
        password="P@ssw0rd",
        host="127.0.0.1",
        port="3306",
        database="reserve"
    )
cur = con.cursor()


letters  = string.ascii_letters
nums = string.digits
sings = string.punctuation
stuffs = letters + nums + sings


class User():
    def __init__(self):
        self._id = random.randint(1000,10000)
        self.__name = "Noname"
        self.__family = "Nofamily"
        self.__phonenumber = "000"
        self.__birth_date = "00/00/00"
        self.__mcode = "____"
        self.__gender = "____"
        self.__username = "User"
        self._password = "".join(random.sample(stuffs,10)).strip()
    
    @property
    def name(self) :
        return self.__name
    @name.setter
    def name(self,value):
        if re.findall(r"^[A-Za-z][a-z]{3,}$", value):
            self.__name = value
    
    @property
    def family(self) :
        return self.__family
    @family.setter
    def family(self,value) :
        if re.findall(r"^[A-Za-z][a-z]{3,}$", value):
            self.__family = value
    
    @property
    def phonenumber(self) :
        return self.__phonenumber
    @phonenumber.setter
    def phonenumber(self,value):
        if re.findall(r"^(?:\+98|09)[0-9]{9}$", value):
            self.__phonenumber = value
    
    @property
    def birth_date(self):
        return self.__birth_date
    @birth_date.setter
    def birth_date(self,value):
        if re.findall(r"^\d{1,2}/\d{1,2}/\d{1,2}$",value):
            self.__birth_date = value
    
    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self,value):
        if value.lower() == "male" or value.lower() == "female":
            self.__gender = value
    @property
    def mcode(self):
        return self.__mcode
    @mcode.setter
    def mcode(self,value):
        if re.findall(r"^[0-9]{10}$", value):
            self.__mcode = value

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self,value):
        if re.findall(r"[A-Za-z0-9]{,15}$",value) :
            self.__username = value
            
class Pation(User):
    def __init__(self):
        super().__init__()
           
class Doctor(User):
    def __init__(self):
        super().__init__()
        self.__specialty = "____"
        self.__degree = "____"
        self.__exp_year = "0"
        self.__medical_code = "0"
        self.__shift_hours = "0-0"
        self.__visit_cost = "00"
        self.__email = "Noemail"
    
    @property
    def specialty(self):
        return self.__specialty
    @specialty.setter
    def specialty(self,value):
        if value in data.specialties:
            self.__specialty = value
    
    @property
    def degree(self):
        return self.__degree
    @degree.setter
    def degree(self,value):
        if value in data.degree:
            self.__degree = value
           
    @property
    def email(self) :
        return self.__email
    @email.setter
    def email(self,value):
        if re.findall(r"^[\w\.-]+@[A-Za-z]+\.[A-Za-z]{2,3}$", value):
            self.__email = value
            
    @property
    def exp_year(self):
        return self.__exp_year
    @exp_year.setter
    def exp_year(self,value):
        if int(value) > 0 :
            self.__exp_year = value
            
    @property
    def medical_code(self):
        return self.__medical_code
    @medical_code.setter
    def medical_code(self,value):
        if len(value) == 10 and value.isdigit :
            self.__medical_code = value
    
    @property
    def shift_hours(self):
        return self.__shift_hours
    @shift_hours.setter
    def shift_hours(self,value):
        if re.findall(r"^(?:[01]\d|2[0-3]):[0-5]\d-(?:[01]\d|2[0-3]):[0-5]\d$",value) :
            self.__shift_hours = value
    
    @property
    def cost(self):
        return self.__visit_cost
    @cost.setter
    def cost(self,value):
        if int(value) > 10 :
            self.__visit_cost = value
            
class visit():
    def __init__(self):
        cur.execute("SELECT d_id FROM doctor")
        self.doctr_lst =[row[0] for row in cur.fetchall()]
        cur.execute("SELECT p_id FROM pation")
        self.pation_lst = [row[0] for row in cur.fetchall()]
        self._id = random.randint(1000,10000)
        self._date = "____"
        self._time = "____"
        self.__visit_cost = "000"
        self.__doctor_id = "____"
        self.__pation_id = "____"
        self._number = 1
        self._status = "Not check"
    @property
    def cost(self):
        return self.__visit_cost
    @cost.setter
    def cost(self,value):
        if int(value) > 50:
            self.__visit_cost = value
    
    @property
    def doctor_id(self):
        return self.__doctor_id
    @doctor_id.setter
    def doctor_id(self,value):
        if value in self.doctr_lst:
            self.__doctor_id = value
    @property
    def pation_id(self):
        return self.__pation_id
    @pation_id.setter
    def pation_id(self,value):
        if value in self.pation_lst:
            self.__pation_id = value
    
    
        
         
   
    
    
    