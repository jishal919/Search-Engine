"""Created on Sun May  2 15:22:38 2021

   @Developer: jishal

Searchengine is still under development


"""
import time

import specs

import multiprocessing

from playsound import playsound

audio = specs.audiopath


BGaudio = multiprocessing.Process(target=playsound, args=(audio,))


BGaudio.start()

file = specs.newborn

specspath = specs.pathOfThisFile

if file == True:


    print("Downloading Aditional Files......\n\n")

    time.sleep(2.5)


    import subprocess

    import sys


    try:

        import cryptography

    except ImportError:

        subprocess.check_call([sys.executable, "-m", "pip", "install", 'cryptography'])

    finally:

        import cryptography

    try:

        import datetime

    except ImportError:

        subprocess.check_call([sys.executable, "-m", "pip", "install", 'datetime'])

    finally:

        import datetime
    try:

        import dotenv

    except ImportError:

        subprocess.check_call([sys.executable, "-m", "pip", "install", 'dotenv'])

    finally:

        import dotenv

    try:

        import playsound

    except ImportError:

        subprocess.check_call([sys.executable, "-m", "pip", "install", 'playsound'])

    finally:

        import playsound

    try:

        import getpass

    except:

        subprocess.check_call([sys.executable, "-m", "pip", "install", 'getpass'])

    finally:

        import getpass

    try:

        import smtplib

    except:

        subprocess.check_call([sys.executable, "-m", "pip", "install", 'smtplib'])

    finally:

        import smtplib

    try:

        import colorama

    except:

        subprocess.check_call([sys.executable, "-m", "pip", "install", 'colorama'])

    finally:

        import colorama

        with open(specspath) as f:

            
            
            fulldata = f.read()

            f.close()

            with open(specspath,'r+') as file:

                file.truncate(0)

            newdata = "newborn = False"

            fulldata = fulldata.replace("newborn = True",newdata)

            with open(specspath,'w') as rightfile:

                rightfile.write(fulldata)

                rightfile.close()



                print("done\n Please restart the program")

else:



    while True:

        from cryptography.fernet import Fernet

        from datetime import datetime

        from dotenv import load_dotenv

        from datetime import date

        from playsound import playsound

        from colorama import Fore , Style

        from time import sleep

        from getpass import getpass

        import multiprocessing

        import platform

        import specs

        import socket

        import random

        import smtplib

        import random

        import banner

        import array

        import json

        import sys

        import os

        version = specs.version

        user = specs.whoami

        versionDetailes = specs.version_details

        Filename = specs.database

        tokens = specs.tokenDatabase

        audio = specs.audiopath

        specspath = specs.pathOfThisFile

        gmailPassword = specs.gmailAppPassword

        gmailID = specs.email

        hostname = socket.gethostname()

        sys_details = socket.gethostbyname_ex(hostname)

        flag = 0

        loop = []

        print("FEEDBACK: mohammedjishal.jasmin@gmail.com")

        now = datetime.now()

        tempfile = specs.tempfile

        key = Fernet.generate_key()

        f_obj =Fernet(key)

        today = date.today()

        date1 = today.strftime("%b-%d-%Y")

        time = now.strftime(" %H:%M:%S")

        colour_nutriliser = banner.colour_nutralised

        loop = 7

        ipadress = ""

        print(colour_nutriliser)

        print("Made with ❤️  by Jishal")

        print("=" *80)

        print(f"Version : {version} \nYou are using {versionDetailes} version of our searchengine") 

        print("=" *80)


        
        user = specs.whoami
        if user == "NULL":
            
                print("\nPlease Login or Sign up to continue ")

                print("\n1 : Login.")

                print("\n2 : Sign up.")

                print("\n3 : Exit.")

                user_Login_or_signup = int(input("\nEnter the Number 1/2/3 :"))

                if user_Login_or_signup == 1:

                    username = str(input("Enter your username :"))

                    if "_SPaCE_" in username:

                        print("This username contains illegal characters , please don't use it")

                    else:
                        

                        username = username.replace(" ","_SPaCE_")
                        
                        login_password = str(input("Enter your password :"))

                        load_dotenv(tokens)
                                    
                        cipher_suite = os.environ.get(username)
                                    
                        cipher_suite = bytes(cipher_suite,'utf-8')

                        
                

                        cipher_suite = Fernet(cipher_suite)
                            

                        with open(Filename) as f:

                            data2 = json.load(f)

                            user_info = data2.get(username)

                        if user_info:


                                saved_password = user_info['Password']

                                loginpass = bytes(saved_password,'utf-8')

                                
                                decoded_text = cipher_suite.decrypt(loginpass)

                                decoded_text = (str(decoded_text,'utf8'))

                                if "_SPaCE_" in decoded_text:

                                    decoded_text = decoded_text.replace("_SPaCE_","")

                                
                        
                                if decoded_text == login_password:

                                    with open(specspath) as f:
                                        
                                        
                                        fulldata = f.read()

                                        f.close()
                                    with open(specspath,'r+') as file:

                                        file.truncate(0)

                                    newdata = "whoami = \""+username+"\""

                                    fulldata = fulldata.replace("whoami = \"NULL\"",newdata)

                
                                    with open(tempfile,'w') as tmpfile:

                                        tmpfile.write(username)

                                        tmpfile.close()
            
                                    with open(specspath,'w') as rightfile:

                                        rightfile.write(fulldata)

                                        rightfile.close()


                                        print("\n\nPlease RESTART the program")

                                        BGaudio.terminate()

                                        sys.exit()

                

                elif user_Login_or_signup == 2:
                    
                    print("fill the following Information\n")

                    name = str(input("Enter your Username : "))

                    if "_SPaCE_" in name:

                        print("This username contains illegal characters , please don't use it")

                    else:
                        

                        name = name.replace(" ","_SPaCE_")
                    

                        if len(name) < 4 :

                            print(" Your name Must be at least 4 characters long , try again")

                            break
                    print("Please enter a valid gmail id , it may need in future issues .")
                    email = str(input("enter your email: "))

                    if "@gmail.com"not in email:

                        print("You have entered an Invalid Email!")
                        break
                    

                    print("1 : Use a custom password")

                    print("2 : Generate a strong password")

                    print("you need to know the email id to delete the data")

                    pass_entering_op = int(input("enter the number 1 / 2 : "))

                    if pass_entering_op == 1:
                        
                        
                        password_ = str(input("enter your password:"))


                    elif pass_entering_op == 2:


                        MAX_LEN = 12
                        
                        DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  

                        LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 

                                            'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',

                                            'r', 's', 't', 'u', 'v', 'w', 'x', 'y',

                                            'z']
                        
                        UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 

                                            'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',

                                            'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',

                                            'Z']
                        
                        SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 

                                '*', '(', ')', '<']
                        
                        COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
                        
                        rand_digit = random.choice(DIGITS)

                        rand_upper = random.choice(UPCASE_CHARACTERS)

                        rand_lower = random.choice(LOCASE_CHARACTERS)

                        rand_symbol = random.choice(SYMBOLS)
                        
                        temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
                        
                        
                        for x in range(MAX_LEN - 4):

                            temp_pass = temp_pass + random.choice(COMBINED_LIST)
                        
                            temp_pass_list = array.array('u', temp_pass)

                            random.shuffle(temp_pass_list)
                    
                        password = ""

                        for x in temp_pass_list:

                                generated_password = password + x
                                
                    
                        password_ = generated_password

                        print(f"your password is {password_}")

                    else:

                        print("invalid input")

                    msg = password_.encode()
            
                    encrpted_pass = f_obj.encrypt(msg)

                    string_encrypted_pass = str(encrpted_pass,'utf8')

                    age = int(input("\nenter the age: "))

                    if age > 5:
                        pass
                    else:

                        print("you age must be at least 5 ")
                    


                    region = str(input("\nenter the region: "))
                    

                    def write_json(data, Filename):

                        with open (Filename,"w") as f:

                            json.dump(data, f,default=str, indent=4)

                    with open (Filename) as json_file:

                        
                        
                        data = json.load(json_file)
                        keyx = str(key,'utf8')
                        

                        if name in data:

                            print(f" The UserName \"{name}\" Is Already been taken by someone ,Please try new one :)")

                    hostname = socket.gethostname()

                    sys_details = socket.gethostbyname_ex(hostname)

                    os = platform.system()

                    date1 = today.strftime("%b-%d-%Y")

                    time = now.strftime(" %H:%M:%S")

                    
                    for Letters in sys_details[2]:

                        ipadress = ipadress + Letters
                        
                    ipadress = ipadress.replace(" ","")

                    data[name] = {'name': name , 'Password' : string_encrypted_pass ,'Email': email ,'age': age, 'region': region ,
                    'Date' : str(date1), 'Time' : str(time), 'OS': os, 'Host name': sys_details[0] , 'ip-adress': ipadress}

                    with open(tokens,'ab') as envfile:

                        unbytedkey = str(key,'utf8')

                        writedtoken = "\n"+name+"="+unbytedkey

                        writedtoken = writedtoken.encode()

                        envfile.write(writedtoken)

                    write_json(data,Filename)
                    
                    print(f"successfully created \'{name}\' ")

                    json_file.close()

                    with open(specspath) as f:

                        loguser = name

                        chngdata = "whoami = \"NULL\""

                        fulldata = f.read()

                        f.close()
                        with open(specspath,'w') as file:

                            file.truncate(0)

                        fulldata = fulldata.replace(chngdata,"whoami = "+"\""+loguser+"\"")
        
                        with open(specspath,'w') as rightfile:

                            rightfile.write(fulldata)
                            
                            rightfile.close()

                        with open(tempfile,'r') as FILe:

                            contents = FILe.read()

                            FILe.close()

                        with open(tempfile,'w') as F:

                            F.close()

                        with open(tempfile,'w') as tmpFile:

                            tmpFile.write(loguser)

                            tmpFile.close()

                            print("Please restart the program")

                            BGaudio.terminate()

                            sys.exit()


                    
                elif user_Login_or_signup == 3:  

                    BGaudio.terminate()

                    sys.exit()

                    
                else:
                    print("Invalid input") 

                    BGaudio.terminate()  

                    flag = 1

        elif len(tempfile) > 3:

                pass   
            
            

                user = specs.whoami

                if user  == "NULL":

                        print("")

                        BGaudio.terminate()

                        break

                else:

                    print("")

                if flag == 0:


                    wlcmsg = user.replace("_SPaCE_"," ")
                    
                    print(f"\n\nWELCOME {wlcmsg}!")

                    print(f"\nYou are signed as {wlcmsg}")

                    print("\n 1 - Search Account.")

                    print("\n 2 - Create Account.")

                    print("\n 3 - Delete My Account.")

                    print("\n 4 - ADMIN MODE.")

                    print("\n 5 - Logout.")

                    print("\n 6 - Exit. \n")

                    operation = int(input("Enter the number 1/2/3/4/5/6 : "))       
                
                

                    if operation == 1:

                        nameOfPerson = str(input(">>> enter the name of the person: "))

                        if "_SPaCE_" in nameOfPerson:

                            print("This username contains illegal characters , please don't use it")

                        else:
                        

                            nameOfPerson = nameOfPerson.replace(" ","_SPaCE_")

                            if len(nameOfPerson) > 60:          

                                print("ERROR \n Your input must be under SIXTY characters.\n try again")  

                        

                        with open(Filename) as f:

                                

                                    data = json.load(f)

                                    user_info = data.get(nameOfPerson)

                                    if user_info:

                                        user_info = data.get(nameOfPerson)

                                        if user_info:

                                            print(user_info)

                                            saved_password = user_info['Password']

                                            name = user_info['name']

                                            age = user_info['age']

                                            region = user_info['region']

                                            date5 = user_info['Date']

                                            saved_time = user_info['Time']

                                            saved_Hostname = user_info['Host name']

                                            saved_ip = user_info['ip-adress']

                                            if "_SPaCE_" in name:

                                                name = name.replace("_SPaCE_"," ")

                                            print (Fore.YELLOW + "\nName :",name,"\n")

                                            print("Age :" , age,"\n")

                                            print("Region :", region,"\n")

                                            print("date Joined :", date5,"\n")

                                            print(colour_nutriliser)

                                        else:

                                            print('Nobody named', nameOfPerson)

                                    else:

                                        print(nameOfPerson,' Does not Exist!')
                    

                    elif operation == 2:

                        print("fill the following Information\n")

                        name = str(input("Enter your Name : "))

                        if "_SPaCE_" in name:

                            print("This username contains illegal characters , please don't use it")

                        else:
                        

                            name = name.replace(" ","_SPaCE_")

                            if len(name) < 4 :

                                print(" Your name Must be at least 4 characters long , try again")

                                break

                        email = str(input("enter your email: "))

                        if "@gmail.com"not in email:

                            print("You have entered an Invalid Email!")

                            break

                        print("1 : Use a custom password")

                        print("2 : Generate a strong password")

                        print("you need to know the email id to delete the data")

                        pass_entering_op = int(input("enter the number 1 / 2 : "))

                        if pass_entering_op == 1:
                            
                            
                            password_ = str(input("enter your password:"))


                        elif pass_entering_op == 2:


                            MAX_LEN = 12
                            
                            DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  

                            LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 

                                                'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',

                                                'r', 's', 't', 'u', 'v', 'w', 'x', 'y',

                                                'z']
                            
                            UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 

                                                'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',

                                                'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',

                                                'Z']
                            
                            SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 

                                    '*', '(', ')', '<']
                            
                            COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
                            
                            rand_digit = random.choice(DIGITS)

                            rand_upper = random.choice(UPCASE_CHARACTERS)

                            rand_lower = random.choice(LOCASE_CHARACTERS)

                            rand_symbol = random.choice(SYMBOLS)
                            
                            temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
                            
                            
                            for x in range(MAX_LEN - 4):

                                temp_pass = temp_pass + random.choice(COMBINED_LIST)
                            
                                temp_pass_list = array.array('u', temp_pass)

                                random.shuffle(temp_pass_list)
                        
                            password = ""

                            for x in temp_pass_list:

                                    generated_password = password + x
                                    
                        
                            password_ = generated_password

                            print(f"your password is {password_}")

                        else:

                            print("invalid input")

                        msg = password_.encode()
                
                        encrpted_pass = f_obj.encrypt(msg)

                        string_encrypted_pass = str(encrpted_pass,'utf8')

                        age = int(input("\nenter the age: "))

                        if age < 5:

                            print("you age must be at least 5 ")
                            break


                        region = str(input("\nenter the region: "))
                        

                        def write_json(data, Filename):

                            with open (Filename,"w") as f:

                                json.dump(data, f,default=str, indent=4)

                        with open (Filename) as json_file:

                            
                            
                            data = json.load(json_file)
                            keyx = str(key,'utf8')
                            

                            if name in data:

                                print(f" The UserName \"{name}\" Is Already been taken by someone ,Please try new one :)")

                            hostname = socket.gethostname()

                            sys_details = socket.gethostbyname_ex(hostname)

                            os = platform.system()

                            date1 = today.strftime("%b-%d-%Y")

                            time = now.strftime(" %H:%M:%S")

                            ipadress = ""

                            for Letters in sys_details[2]:

                                ipadress = ipadress + Letters
                            
                                ipadress = ipadress.replace(" ","")
                    
                        data[name] = {'name': name , 'Password' : string_encrypted_pass ,'Email': email ,'age': age, 'region': region ,
                        'Date' : str(date1), 'Time' : str(time), 'OS': os, 'Host name': sys_details[0] , 'ip-adress': ipadress}

                        with open(tokens,'ab') as envfile:

                            unbytedkey = str(key,'utf8')

                            writedtoken = "\n"+name+"="+unbytedkey

                            writedtoken = writedtoken.encode()

                            envfile.write(writedtoken)

                        write_json(data,Filename)
                        
                        print(f"successfully created \'{name}\' ")

                        json_file.close()

                 

                    elif operation == 3:

                        print("enter the name of the person to delete")

                        deleting_data = str(input("enter the name: ")) 

                        if "_SPaCE_" in deleting_data:

                            print("This username contains illegal characters , please don't use it")

                        else:
                        

                            deleting_data = deleting_data.replace(" ","_SPaCE_")  

                            if len(deleting_data) > 60:

                                print("Username must be under SIXTY letters") 
                        

                        with open(Filename) as f:

                            data2 = json.load(f)

                            user_info = data2.get(deleting_data)

                            if user_info:

                                user_info = data2.get(deleting_data)

                                if user_info:

                                    saved_password = user_info['Password']

                                    saved_password = bytes(saved_password,'utf-8')
                                    

                                    pass_verify = str(input("enter the password: "))

                                    load_dotenv(tokens)
                                    
                                    cipher_suite = os.environ.get(deleting_data)
                                    
                                    cipher_suite = bytes(cipher_suite,'utf-8')
                

                                    cipher_suite = Fernet(cipher_suite)
                                    
                                    
                                    encoded_text2 = saved_password

                                    decoded_text = cipher_suite.decrypt(encoded_text2)

                                    decoded_text = (str(decoded_text,'utf8'))

                                    
                                    if decoded_text == pass_verify:

                                        def delete_data(data, Filename):

                                            with open (Filename,"w") as f:

                                                json.dump(data, f, indent=4)

                                        with open (Filename) as json_file:

                                            data = json.load(json_file)

                                            if deleting_data in data:

                                                del data[deleting_data]       

                                                delete_data(data)   

                                                del os.environ[deleting_data]                                      

                                                load_dotenv(tokens)

                                                dlttoken = os.environ.get(deleting_data)

                                                print(f"\n\nSUCCESSFULLY DELETED \'{deleting_data}\'") 

                                                with open(tempfile,'r') as FILe:

                                                    contents = FILe.read()

                                                    FILe.close()

                                                    loguser= contents

                                                if loguser == deleting_data:
                                                
                                                    with open(specspath) as f:

                                                        chngdata = "whoami = "+"\""+loguser+"\""

                                                        fulldata = f.read()

                                                        f.close()

                                                        with open(specspath,'w') as file:

                                                            file.truncate(0)

                                                        fulldata = fulldata.replace(chngdata,"whoami = \"NULL\"")
                                        
                                                        with open(specspath,'w') as rightfile:

                                                            rightfile.write(fulldata)
                                                            
                                                            rightfile.close()

                                                            with open(tempfile,'w') as tmpfile:

                                                                tmpfile.close()

                                                                break       

                                    else:

                                        print("Invalid password")

                                        print("1 ; Forget password")

                                        print("2 ; leave")  

                                        forget_operation = int(input("enter the number 1/2: "))

                                        if forget_operation == 1:

                                            print("proccing.....")

                                            print("please wait...........")

                                            sleep(3)

                                            forget_deleting_data = deleting_data

                                            def delete_data(data,Filename):

                                                with open (Filename,"w") as f:

                                                    json.dump(data, f, indent=4)

                                            with open (Filename) as json_file:

                                                data = json.load(json_file)

                                                forget_user_info = data.get(deleting_data)

                                                if forget_user_info:

                                                        forget_user_info = data.get(deleting_data)

                                                        if forget_user_info:

                                                                saved_email = forget_user_info['Email']

                                                                receiver = saved_email

                                                                

                                                                server=smtplib.SMTP('smtp.gmail.com',587)

                                                                 

                                                                server.starttls()

                                                                

                                                                password = gmailPassword

                                                                server.login(gmailID,password)                        

                                                                otp=''.join([str(random.randint(0,9)) for i in range(4)])

                                                                otpmsg='SEARCHENGINE \n This is Your OTP '+ str(otp)+' for deleting your account,\"'+deleting_data+'\" \n Do not share this with anyone \n OTP provided by SEARCHENGINE \n Feedback : mohammedjishal.jasmin@gmail.com'
                                                                
                                                                
                                                                server.sendmail(gmailID,receiver,otpmsg)
                                                                
                                                                server.quit()   

                                                                print("We have sent an otp to your Email adress , Please enter it below")                                        
                                                                
                                                                check_otp = input("enter the otp:")

                                                                if check_otp == otp:

                                                                    def delete_data(data, Filename):

                                                                        with open (Filename,"w") as f:

                                                                            json.dump(data, f, indent=4)

                                                                    with open (Filename) as json_file:

                                                                        data = json.load(json_file)

                                                        

                                                                        if deleting_data in data:

                                                                            del data[deleting_data]

                                                                            delete_data(data)     

                                                                            del os.environ[deleting_data]    

                                                                            load_dotenv(tokens)

                                                                            dlttoken = os.environ.get(deleting_data)

                                                                            print(f"Successfully deleted {forget_deleting_data}")

                                                                        else:                                       

                                                                            print(f"no one named {forget_deleting_data}")

                                                                            break
                                                                else:

                                                                    print("You have entered the wrong otp!")

                                                                    break
                                                        else:                                   

                                                                print("you entered the wrong otp , try again")

                                                                break
                                                        
                                                            
                                        elif forget_operation == 2:               

                                            print("cancelled")    

                                            BGaudio.terminate()           

                                            sys.exit()                    

                                        else:                

                                            print("invalid input ,  try again")


                                else:
                                    print("Oops. Something went wrong , try again later [code 865]")

                            else:
                                print("Oops. Something went wrong , try again later  [code 868]")

                                                        

                    elif operation == 4:                        

                        print("Entering Administrator mode ")   

                        print("\n NOTE : ADMIN MODE is only for the creator\n")         

                        

                        administrator_inp = getpass("Enter the administration password: ") 

                        token5 = specs.at   

                        token5 = token5.encode()

                        token6 = Fernet(token5)    

                        encAT = "gAAAAABi7TZ_lOYymSNv6yB7mspbRRh2pbCyxjj1MLnDx_nJ2Gjl2hKL0Qx7ofT2Ps_UXeJmlOmC9GiccNHm2zGU1v4zg_h2Ow==".encode()

                        token7 = token6.decrypt(encAT) 

                        token7 = token7.decode()

                        if administrator_inp == token7:   

                            loop = 10         

                            print("welcome")

                            while True:

                                print("You are now an ADMIN")

                                print("\n 1 - View a account")

                                print(" 2 - Edit someone's account")              

                                print(" 3 - Delete account")

                                print(" 4 - Exit ADMIN MODE")

                                admin_choice = int(input("enter the number 1/2/3/4 : "))                

                                if admin_choice == 1:

                                    user_admin = str(input("enter the name of the account: "))

                                    if "_SPaCE_" in user_admin:

                                        print("This username contains illegal characters , please don't use it")

                                    else:
                        

                                        user_admin = user_admin.replace(" ","_SPaCE_")

                                        if len(user_admin) > 60:

                                            print("Username must be under SIXTY letters")

                                            break
                                    

                                    with open(Filename) as f:

                                      
                                      

                                            data = json.load(f)


                                            user_info = data.get(user_admin)

                                            if user_info:

                                                user_info = data.get(user_admin)

                                                if user_info:

                                                    saved_password = user_info['Password']

                                                    name = user_info['name']

                                                    if "_SPaCE_" in name:

                                                        name = name.replace("_SPaCE_"," ")

                                                    try:

                                                        saved_email = user_info['Email']

                                                    except:

                                                        print()

                                                    age = user_info['age']

                                                    try:
                                                        savedOS = user_info['OS']
                                                    except:
                                                        print()
        
                                                    region = user_info['region']

                                                    date = user_info['Date']

                                                    saved_time = user_info['Time']

                                                    saved_Password = user_info['Password']

                                                    try:

                                                        o_s = user_info['OS']

                                                    except:

                                                        print("")

                                                    saved_Hostname = user_info['Host name']

                                                    saved_ip = user_info['ip-adress']

                                                    
                                                    print (Fore.YELLOW + "\nName :",name)

                                                    try:

                                                        print("Email: ",saved_email)

                                                    except:

                                                        print("Age :" , age)

                                                    print("Age :" , age)

                                                    print("Region :", region)


                                                    print("Joined date : ", date)

                                                    print("Joined time : ",saved_time)

                                                    try:        

                                                        print("Operating system : ",o_s)

                                                    except:
                                            
                                                        print()

                                                    print("Host name :",saved_Hostname)


                                                    print("IP-Adress :",saved_ip)

                                                    print(colour_nutriliser)

                                            

                                elif admin_choice == 2:              

                                    print("fill the following data\n")                  

                                    Editname = str(input("enter the name of the person: "))

                                    if "_SPaCE_" in Editname:

                                        print("This username contains illegal characters , please don't use it")

                                    else:
                        

                                        Editname = Editname.replace(" ","_SPaCE_")

                                        if len(Editname) > 60:

                                            print("Username must be under SIXTY letters")
                                    

                                    if len(Editname) < 4 :                 

                                        print(" Your name Must be at least 4 characters long , try again")                      

                                        break                       

                                    Editage = int(input("\nenter the age: "))                      

                                    Editregion = str(input("\nenter the region: "))          

                                    def write_ADMIN_json(data, Filename):                   

                                        with open (Filename,"w") as f:                     

                                            json.dump(data, f,default=str, indent=4)  

                                    with open (Filename) as json_file:                   

                                        data = json.load(json_file)   
                    
                                    data[name] = {'name': Editname , 'Password' : saved_password , 'age': Editage, 'region': Editregion , 'Date' : str(date1), 'Time' : str(time), 'Host name': sys_details[0] , 'ip-adress': sys_details[2]}     

                                    write_ADMIN_json(data) 
                                                

                                    print(f"successfully Edited \'{name}\' to the database")
                                    

                                elif admin_choice == 3:        

                                    print("enter the name of the person to delete")            

                                    deleting_ADMIN_data = str(input("enter the name: "))  

                                    if "_SPaCE_" not in deleting_ADMIN_data:

                                        pass
                                        

                                    else:
                                        print("This username contains illegal characters , please don't use it")

                                    deleting_ADMIN_data = deleting_ADMIN_data.replace(" ","_SPaCE_")

                        

                                    with open(Filename) as f:

                                            data2 = json.load(f)

                                            user_info = data2.get(deleting_ADMIN_data)

                                            if user_info:

                                                user_info = data2.get(deleting_ADMIN_data)

                                                
                                                def delete_data(data, Filename):

                                                    with open (Filename,"w") as f:

                                                        json.dump(data, f, indent=4)

                                                with open (Filename) as json_file:

                                                    data = json.load(json_file)

                                                    if deleting_ADMIN_data in data:

                                                        del data[deleting_ADMIN_data] 

                                                        delete_data(data,Filename) 

                                                        load_dotenv(tokens)

                                                        dlttoken = os.environ.get(deleting_ADMIN_data)

                                                        print(f"\n\nSUCCESSFULLY DELETED \'{deleting_ADMIN_data}\'") 

                                                        with open(tempfile,'r') as FILe:

                                                            contents = FILe.read()

                                                            FILe.close()

                                                            loguser= contents

                                                        if loguser == deleting_ADMIN_data:
                                                        
                                                            with open(specspath) as f:

                                                                chngdata = "whoami = "+"\""+loguser+"\""

                                                                fulldata = f.read()

                                                                f.close()

                                                                with open(specspath,'w') as file:

                                                                    file.truncate(0)

                                                                fulldata = fulldata.replace(chngdata,"whoami = \"NULL\"")
                                                
                                                                with open(specspath,'w') as rightfile:

                                                                    rightfile.write(fulldata)
                                                                    
                                                                    rightfile.close()

                                                                    with open(tempfile,'w') as tmpfile:

                                                                        tmpfile.close()

                                                                        break
                                                                        

                                            
                                elif admin_choice == 4:

                                    BGaudio.terminate() 

                                    sys.exit()
                        else:
                            print("\ninvalid password")

                    elif operation == 5:

                        with open(tempfile,'r') as FILe:

                            contents = FILe.read()

                            FILe.close()

                        loguser= contents

                        print(f"\nAre you sure that you want to logout from {loguser}!") 

                        print("\n 1 : YES\n\n 2 : NO\n")

                        logoutChoice = int(input("Enter the number :"))

                        if logoutChoice == 1:

                            with open(specspath) as f:

                                chngdata = "whoami = "+"\""+loguser+"\""

                                fulldata = f.read()

                                f.close()

                                with open(specspath,'w') as file:

                                    file.truncate(0)

                                fulldata = fulldata.replace(chngdata,"whoami = \"NULL\"")

                
                                with open(specspath,'w') as rightfile:

                                    rightfile.write(fulldata)
                                    
                                    rightfile.close()
                                    
                                    with open(tempfile,'w') as tmpfile:

                                        tmpfile.close()

                                    print(f"\nsuccessfully Logout from {loguser}!")

                                    flag = 1

                                    BGaudio.terminate()

                                    sys.exit()
                                    
                                    
                                    
                        elif logoutChoice == 2:

                            print("Done !")
                            


                                                    
                    elif operation == 6:

                        BGaudio.terminate() 

                        sys.exit()

                    else:

                        print("You can only enter number 1/2/3/4/5:")
                        break

        else:
            print("Something Went wrong , Please download it again and delete current file")                