import re
from datetime import datetime
import random
import string
import hashlib

letters  = string.ascii_letters
nums = string.digits
sings = string.punctuation
stuffs = letters + nums + sings

banks = ["622106","639347","627353","621986", "610433", "603799", "589210",
         "502806" "627648", "628023","502908"]
tar_cate = [
    "Food & Restaurants",
    "Supermarkets",
    "Transportation",
    "Healthcare",
    "Entertainment",
    "Internet",
    "Education",
    "Gifts & Donations",
    "Home",
    "Loans",
    "Taxes",
    "Travel",
    "Vacation",
    "Subscriptions",
    "Investments",
    "Others"
]
banks_name = {
    "622106": "Parsian Bank",
    "639347": "Pasargad Bank",
    "627353": "Tejarat Bank",
    "621986": "Saman Bank",
    "610433": "Mellat Bank",
    "603799": "Melli Bank",
    "589210": "Sepah Bank",
    "502806": "Shahr Bank",
    "627648": "Saderat Bank",
    "628023": "Maskan Bank",
    "502908" : "Taavon"
}

class person :
    def __init__(self):
        self.id = random.randint(1000,10000)
        self.__name = "NoName"
        self.__family = "NoFamily"
        self.__mobile = "01234567890"
        self.__username = "NoUser"
        self.password = "0000"

    @property
    def name(self) :
        return self.__name
    @name.setter
    def name(self,value) : 
        if re.findall(r"^[A-Za-z]{3,}$", value):
            self.__name = value

    @property
    def family(self):
        return self.__family

    @family.setter
    def family(self, value):
        if re.findall(r"^[A-Za-z][a-z]{3,}$", value):
            self.__family = value
    
    @property
    def mobile(self):
        return self.__mobile

    @mobile.setter
    def mobile(self, value):
        if re.findall(r"^(?:\+98|09)[0-9]{9}$", value):
            self.__mobile = value
    @property
    def username(self) :
        return self.__username
    @username.setter
    def username(self,value) :
        if re.findall(r"[A-Za-z0-9]{,15}$",value) :
            self.__username = value
    
class card :
    def __init__(self):
        self.__ownerId = "000"
        self.cardId = random.randint(1000,10000)
        self.__Cnumber = "1111222233334444" 
        self.__ownerName = "nonmae"
        self.__expdate = "01/01"
        self.__cvv2 = "1111"
        self.__bankName = "Nobank" 
        self.value = 0
    @property
    def Cnumber(self):
        return self.__Cnumber
    @Cnumber.setter
    def Cnumber(self,value):
        if len(value) == 16 and value[0:6] in banks:
            self.__Cnumber = value
    @property
    def ownerName(self):
        return self.__ownerName
    @ownerName.setter
    def ownerName(self,value) :
        if re.findall(r"^[A-Za-z]{3,}$", value):
            self.__ownerName = value
    @property
    def expdate(self) :
        return self.__expdate
    @expdate.setter
    def expdate(self,value) :
        if re.findall(r"^(0[1-9]|1[0-2])\/\d{2}$",value) :
            self.__expdate = value
    @property
    def cvv2(self):
        return self.__cvv2
    @cvv2.setter
    def cvv2(self,value) :
        if re.findall(r"^\d{3,4}$",value) :
            self.__cvv2 = value
    @property
    def bankName(self) :
        return self.__bankName
    @bankName.setter
    def bankName(self,value)  :
        if value in list(banks_name.values()) :
            self.__bankName = value
    @property
    def ownerId(self):
        return self.__ownerId
    @ownerId.setter
    def ownerId(self,value) :
        if len(value) == 4 :
            self.__ownerId = value             
    
class tarakonesh :
    def __init__(self):
        self.T_id = random.randint(1000,10000)
        self.T_date = datetime.now()
        self.__T_value = 0
        self.__T_type = "Notype"
        self.__reaseon = "NoReaseon"
    @property
    def T_type(self) :
        return self.__T_type
    @T_type.setter
    def T_type(self,value) :
        if value == "decrease" or value == "increase" : 
            self.__T_type = value
    @property
    def T_value(self) :
        return self.__T_value
    @T_value.setter
    def T_value(self,value) :
        if value > 0:
            self.__T_value = value
    @property
    def reaseon(self) :
        return self.__reaseon
    @reaseon.setter
    def reaseon(self,value) :
        if value.title() in tar_cate : 
            self.__reaseon = value
         
          
