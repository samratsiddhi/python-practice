islogin = False
exit = 0
users = []

def register():
    error = 0
    while error ==0:
        username = input("Enter username : ")
        
        #checking username validity 
        if len(username)==0:
            print("Must enter username")
            continue
        
        #check for duplicate user name
        user_name_duplicate = 0
        for user in users:
            if username == user['username']:
                user_name_duplicate = 1
        
        #if username is duplicate
        if user_name_duplicate==1:
            print(f"user {username} already exists try again")
            continue
                
            
        password = input("Enter password : ")
        
        #checking password validity 
        if len(password)<4:
            print("Password must be atleast 4 letters")
            continue
        
        confirm_password = input("Enter confirm password : ")
        
        #checking password validity
        if password != confirm_password:
            print("password does not match try again")  
            continue
        else:
            user = {
                    "username": username,
                    "password": password
                    }
            users.append(user)
            
            print(f"user {username} successfully registered")
        
        #to end loop
        error = 1

def login():
    error = 0
    global islogin
    while error == 0 :
        #taking input for username and password
        username = input("Enter user name : ")
        password = input("Enter password : ")
        
        found = 0
        
        #looping through all credentials
        for credentials in users:
            #checking for username
            if credentials['username'] == username:
                found = 1
                #after username is found checking the password for that user
                if credentials['password'] == password:
                    print("Login successfull")
                    error = 1
                    #change login status
                    islogin = True
                else:
                    print("incorrect password try again") 
                    continue
        #if username not found
        if found == 0 :
            print("User does not exist please register first")    
            register()  
            print("you can now login")      


while exit ==0:
    
    #if no user in logged in
    if islogin == False:
        print("Welcome to an authentication CLI")
        status = int(input("""
                        Press 1 for login
                        Press 2 for registration
                        Press 3 to exit system
                        """))
        
        #for registartion
        if status == 2: 
            register_more = 0
            while register_more == 0:
                register()
                more = input("Do you want to register more users? (yes/no)")
                if(more == "no"):
                    register_more = 1
        
        #for login
        elif status == 1:
            login() 
        
        #for exiting the system
        elif status ==3 :
            print("exiting system")
            exit = 1 
        else:
            print("invalid input")
    # if user is logged in
    else:
        while islogin == True:
            logout = input("Do you want to logout(yes/no)?")
            if logout == "yes":
                islogin = False
                print("Successfully logged out")
                
            
        

        
        



        