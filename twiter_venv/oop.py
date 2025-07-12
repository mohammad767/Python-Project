import random
import string
import re
import pymongo
import datetime


letters  = string.ascii_letters
nums = string.digits
sings = string.punctuation
stuffs = letters + nums + sings


class User :
    def __init__(self):
        self.user_id = random.randint(1000,10000)
        self.__name = "NoName"
        self.__family = "NoFamily"
        self.__mobile = "0000"
        self.__email = "NoEmail"
        self.followers = 0
        self.following = 0
        self.followers_lst = []
        self.following_lst = []
        self.__username = "NoUser"
        self.password =  "".join(random.sample(stuffs,10))
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
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if re.findall(r"^[\w\.-]+@[A-Za-z]+\.[A-Za-z]{2,3}$", value):
            self.__email = value

    @property
    def username(self) :
        return self.__username
    @username.setter
    def username(self,value) :
        if re.findall(r"[A-Za-z0-9]{,15}$",value) :
            self.__username = value
    
        
class twit :
    def __init__(self):
        self.__user_twit = "NOUser"
        self.twit_id = random.randint(1000,10000)
        self.__twit = "NoTwit"
        self.__mention = "NOMention"
        self.__hashtag = "NoHashtag"
        self.tiwt_date = datetime.datetime.now()
        self.like = 0
        self.dislike = 0
        self.__comment = "Nocomment"
        
        
    @property
    def user_twit(self) :
        return self.__user_twit
    @user_twit.setter
    def user_twit(self,value) :
        if self.__user_twit == "NO" :
            self.__user_twit = ""
        else :
            con = pymongo.MongoClient("mongodb://localhost:27017")
            db = con["Mini_Twiter"]
            col = db["Users"]
            info = list(col.find({"username" : value}))
            if info : 
                self.__user_twit = value
    @property
    def twit(self) :
        return self.__twit
    @twit.setter
    def twit(self,value) :
        if re.findall(r"[A-Za-z0-9!@#$%?.;:(){}]{,100}$",value) :
            self.__twit = value
    
    @property
    def mention(self) : 
        return self.__mention
    @mention.setter
    def mention(self,value) :
        if self.__mention == "NO" :
            self.__mention = ""
        else :
            con = pymongo.MongoClient("mongodb://localhost:27017")
            db = con["Mini_Twiter"]
            col = db["Users"]
            info = list(col.find({"username" : value}))
            if info : 
                self.__mention = value
    
    @property
    def hashtag(self) :
        return self.__hashtag
    @hashtag.setter
    def hashtag(self,value) :
        if re.findall(r"^[#][A-Za-z0-9]",value) :
            self.__hashtag = value
    
    @property
    def comment(self) :
        return self.__comment
    @comment.setter
    def comment(self,value) :
        if re.findall(r"[A-Za-z0-9!?.:]{,30}$",value) :
            self.__comment = value