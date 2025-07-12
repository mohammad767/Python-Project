from colorama import init, Fore
init(autoreset=True)
import oop
import pymongo
import random

def create_acc() :
    con = pymongo.MongoClient("mongodb://localhost:27017")
    db = con["Mini_Twiter"]
    col = db["Users"]
    us = oop.User()
    us.name = input("Enter your name : ")
    us.family = input("Enter your family : ")
   
    while True:
        
        us.mobile = input("Enter your mobile number: ")
        m = us.mobile
        valid_local = m.startswith("09") and len(m) == 11 and m.isdigit()
        valid_inter = m.startswith("+98") and len(m) == 13 and m[1:].isdigit()
        
        if valid_local or valid_inter:
            mob_lst = list(col.find({"mobile" : us.mobile}))
            #print(mob_lst)
            if mob_lst == [] :
                break
            
            if mob_lst[0].get("mobile") == us.mobile:
                print(Fore.RED+"This mobile number is used.")
        else:
            print(Fore.RED+"Invalid mobile number. Try again.")

        
    while True :
        us.email = input("Enter your email : ")
    
        email_lst = list(col.find({"email" : us.email}))
        if email_lst == [] :
            break
        
        if email_lst[0].get("email") == us.email :
            print("This email is already used")
            us.email = input("Enter your email : ")
        
    us.username = input("Enter your username : ")
    user_lst = list(col.find({"username" : us.username}))
    while True :
        if user_lst == [] :
            break
        
        if user_lst[0].get("username") == us.username : 
            print("This username is already taken try new one")
            us.username = input("Enter your username : ")
                
    date = {"id" : us.user_id,"name" : us.name.title(),"family": us.family.title(),
            "mobile" : us.mobile,"email": us.email,"username" : us.username,
            "password" : us.password,"followers_num": us.followers,"following_num" : us.following,
            "followers" : us.followers_lst,"following" : us.following_lst}
    col.insert_one(date)
    print(Fore.WHITE+f"Password : {us.password} , ",Fore.WHITE+f"Username: {us.username}")
    print("User add✅")
     
def login() :
    user_n = input("Enter your username : ")
    passw = input("Enter your password : ")
    
    con = pymongo.MongoClient("mongodb://localhost:27017")
    db = con["Mini_Twiter"]
    col = db["Users"]
    info = list(col.find({"$and" :[{"username" : user_n},{"password":passw}]}))
    #print(info)
    
    if info == [] :
        while True :
            print(Fore.RED+"Invalid username or password")
            user_n = input("Enter your username : ")
            passw = input("Enter your password : ")
            con = pymongo.MongoClient("mongodb://localhost:27017")
            db = con["Mini_Twiter"]
            col = db["Users"]
            info = list(col.find({"$and" :[{"username" : user_n},{"password":passw}]}))
            if info != [] :
                break
            
    else :
        while True :
            print(f"Welcome {info[0]['username']} ")
            print(Fore.CYAN+"w --> write twit")
            print(Fore.CYAN+"r --> read twit")
            print(Fore.CYAN+"e --> expelor")
            print(Fore.CYAN+"s --> search profile")
            print(Fore.CYAN+"v --> viwe profile")
            print(Fore.RED+"x --> exit")
            print(Fore.GREEN+"-"*15)
            user = info[0]["username"]
            #print(user)
            ch = input("Enter your choice : ").lower()
            if ch == "w" :
                write(user)
            if ch == "r" :
                read(user)
            if ch == "e" :
                expelor(user)
            if ch == "s" :
                search(user)
            if ch == "v" :
                viwe_profile(user)
            if ch == "x" :
                print(Fore.YELLOW+"Goodbye")
                break
            
def write(user) :
    tw = oop.twit()
    con = pymongo.MongoClient("mongodb://localhost:27017")
    db = con["Mini_Twiter"]
    col = db["Twit"]
    tw.user_twit = user
    tw.twit = input("Enter your twit(limit 100) : ")
    while len(tw.twit) > 100 :
        print(Fore.YELLOW+"Too long,please make it short")
        tw.twit = input("Enter your twit(limit 100) : ")
    b_words = ["fuck","motherfucker","asshole","dick"]
    c = 1
    while c < 4  :
        for i in b_words :
            if i in tw.twit :
                print(Fore.RED+"we found illegal word in your twit !! please write it coretly ")
                tw.twit = input("Enter your twit(limit 100) : ")
            c += 1
    mention = input("Do you want mention someone(N/Y) ? ").lower()
    if mention == "n" :
        tw.mention = "NO"
    if mention == "y" :
        tw.mention = input("Enter the username want mention : ")
        col2 = db["Users"]
        info = list(col2.find({"username" : tw.mention}))
        while True :
            if info == [] :
                print(Fore.RED+"Invalid user,try again")
                tw.mention = input("Enter the username want mention : ")
                #col2 = db["Users"]
                info = list(col2.find({"username" : tw.mention}))
            if info :
                break
    
    
    
    tw.hashtag = input("Enter the name of the hashtag : ")
    data = {"t_id" : tw.twit_id,"username" : tw.user_twit,"twit" : tw.twit,
            "mention" : tw.mention,"hashtag" : tw.hashtag,
            "comment" : [],"like" : tw.like,"dislike" : tw.dislike,
            "p_date" : tw.tiwt_date}
    col.insert_one(data)
    print("Done✅")
    
def comment(user) :
    tw = oop.twit()
    id = int(input("Enter the id of the twit : "))
    con = pymongo.MongoClient("mongodb://localhost:27017")
    db = con["Mini_Twiter"]  
    col = db["Twit"]
    info = list(col.find({"t_id" : id}))
    print("r --> read comment")
    print("w --> write comment")
    print(Fore.RED+"x --> exit")
    print(Fore.GREEN+"-"*15)
    ch = input("Enter your choice : ").lower()
    if ch == "w" :
        #print(info)
        while True :
            if info == [] :
                print("Wrong id")
                id = input("Enter the id of the twit : ")
                info = list(col.find({"id" : id}))
            if info != [] :
                comm = info[0]["comment"]
                tw.comment = input("Enter your comment (limit 50) : ")
                while len(tw.comment) > 50 :
                    print(Fore.YELLOW+"Too long,please make it short")
                    tw.comment = input("Enter your twit(limit 100) : ")
                b_words = ["fuck","motherfucker","asshole","dick"]
                c = 1
                while c < 4  :
                    for i in b_words :
                        if i in tw.comment :
                            print(Fore.RED+"we found illegal word in your twit !! please write it coretly ")
                            tw.comment = input("Enter your twit(limit 100) : ")
                        c += 1
                
                comment = {user :tw.comment }
                comm.append(comment)
                filter = {"t_id" : id}
                new_val = {"$set":{"comment" : comm}}
                col.update_one(filter,new_val)
                print("Done")
                break
    if ch == "r" :
        comment_ = info[0]["comment"]
        for i in comment_ :
            cont = list(i.items())
            print(f"{cont[0][0]} : {cont[0][1]}")
            print(Fore.GREEN+"-"*15)
          
def viwe_profile(user) :
    con = pymongo.MongoClient("mongodb://localhost:27017")
    db = con["Mini_Twiter"]  
    col = db["Twit"]
    col2 = db["Users"]
    info = list(col.find({"username" : user}))
    info2 = list(col2.find({"username" : user}))
    if info == [] or info2 == [] :
        print("There is no things")
    else :
        print(f"followers : {info2[0]['followers_num']}  following : {info2[0]['following_num']}") 
        print(Fore.RED+"*"*15)
        j = 1
        for i in info :
            print(f"{j}-{i['twit']}")
            print(f"Like : {i['like']}  Dislike : {i['dislike']}")
            print(f"ID : {i['t_id']}")
            print(Fore.GREEN+"-"*15)
            j+=1
        ch = input("Do you want see comments(Y/N) : ").lower()
        if ch == "n" :
            print("OK,goodbye")
        if ch == "y" :
            t_id = int(input("Enter the twit id : "))
            info = list(col.find({"t_id" : t_id}))
            comment_ = info[0]["comment"]
            for i in comment_ :
                cont = list(i.items())
                print(f"{cont[0][0]} : {cont[0][1]}")
                print(Fore.GREEN+"-"*15)
            
def like() :
    id = int(input("Enter the id of the twit : "))
    con = pymongo.MongoClient("mongodb://localhost:27017")
    db = con["Mini_Twiter"]  
    col = db["Twit"]
    info = list(col.find({"t_id" : id}))
    while True :
        if info == [] :
            print("Wrong id")
            id = input("Enter the id of the twit : ")
            info = list(col.find({"id" : id}))
        if info != [] :
            ch = input("You want like or dislike : ").lower()
            if ch == "like" :
                like = info[0]["like"]
                like += 1
                filter = {"t_id" : id}
                new_val = {"$set" : {"like" : like}}
                col.update_one(filter,new_val)
                print(Fore.GREEN+"Done")
                break
            if ch == "dislike" : 
                dislike = info[0]["dislike"]
                dislike += 1
                filter = {"t_id" : id}
                new_val = {"$set" : {"dislike" : dislike}}
                col.update_one(filter,new_val)
                print(Fore.RED+"Done")
                break
    print("Done")
  
def expelor(user) :
    con = pymongo.MongoClient("mongodb://localhost:27017")
    db = con["Mini_Twiter"]  
    col = db["Twit"]
    info = list(col.find())
    random.shuffle(info)
    for slice in info :
        print(f"User: {slice['username']}")
        print(slice["twit"])
        print(f"ID: {slice['t_id']}   {slice['p_date']}")
        print(Fore.GREEN+"-"*15)
    print("l --> like or dislike")
    print("c --> comment")
    ch = input("Enter your choice : ").lower()
    if ch == "l" :
        like()
    if ch == "c" :
        comment(user)
    
def read(user) :
    con = pymongo.MongoClient("mongodb://localhost:27017")
    db = con["Mini_Twiter"]   
    col = db["Users"]
    col2 = db["Twit"]
    info = list(col.find({"username" : user}))
    fol = info[0]["following"]
    if fol == [] :
        print(Fore.YELLOW+"You dont follow anybody")
    else :
        for i in fol :
            info2 = list(col2.find({"username" : i}))
            for j in range(len(info2)) :
                print(f"{info2[j]['username']} :")
                print(f"{j+1}-{info2[j]['twit']}")
                print(f"ID : {info2[j]['t_id']}")
                print(Fore.CYAN+"-"*20)
        print("l --> like or dislike")
        print("c --> comment")
        ch = input("Enter your choice : ").lower()
        if ch == "l" :
            like()
        if ch == "c" :
            comment(user)

def follow(user,user2) : 
    while True :
        con = pymongo.MongoClient("mongodb://localhost:27017")
        db = con["Mini_Twiter"]
        col = db["Users"]
        info = list(col.find({"username" : user}))
        follower = info[0]["followers"]
        if user2 in follower : 
            print(Fore.YELLOW+"This person in alreafy in followers")
            break
        follower.append(user2)
        
        
        follower_n = info[0]["followers_num"]
        follower_n += 1 
        
        filter = {"username" : user}
        new_val = {"$set" :{"followers" : follower ,"followers_num" : follower_n}}
        col.update_one(filter,new_val)
        
        print("Done")
        info = list(col.find({"username" : user2}))
        following = info[0]["following"]
        following.append(user)
        
        following_n = info[0]["following_num"]
        following_n += 1 
        
        filter = {"username" : user2}
        new_val = {"$set" : {"following" : following , "following_num" : following_n}}
        col.update_one(filter,new_val)
        print(Fore.GREEN+"Done")
        break
    
def read_s(user) : 
    con = pymongo.MongoClient("mongodb://localhost:27017")
    db = con["Mini_Twiter"]   
    col = db["Twit"]
    info = list(col.find({"username" : user}))
    if info == [] :
        print("There is no twit")
    else :
        for i in range(len(info)) :
            print(user)
            print(f"{i+1}-{info[i]['twit']}")
            print(f"ID: {info[i]['t_id']}")
            print(Fore.CYAN+"-"*20)
        print("l --> like or dislike")
        print("c --> comment")
        ch = input("Enter your choice : ").lower()
        if ch == "l" :
            like()
        if ch == "c" :
            comment(user)
         
def search(user) :
    con = pymongo.MongoClient("mongodb://localhost:27017")
    db = con["Mini_Twiter"]
    col = db["Users"]
    s_user = input("Enter the username you want search : ")
    info = list(col.find({"username" : {"$regex" : f"^{s_user}"}}))
    for i in range(len(info)) :
        print(f"ID: {info[i]['id']}  Username: {info[i]['username']}")
        print(Fore.BLUE+"-"*15)
    r_user = input("Enter the user you want : ")
    info = list(col.find({"username" : r_user}))
    if info :
        print("f --> following")
        print("r --> read user twit")
        ch =  input("Enter your choice : ").lower()
        if ch == "f" :
            follow(r_user,user)
        if ch == "r" :
            read_s(r_user)
        
    else : 
        print("Invalid username")
