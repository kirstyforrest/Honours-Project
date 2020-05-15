from tkinter import*
import os

#root = Tk()
Users = ""
Junior = ""
Global = ""
Users_Selected = ""

def delete2():
    screen3.destroy()
    
def delete3():
    screen4.destroy()

def delete4():
    screen5.destroy()

def ACL(username1):


    list_of_files = os.listdir()
    if username1 in list_of_files:
        file2 = open(username1, "r")
        verify = file2.read().splitlines()
        print(verify)
        if "User" in verify or "Client" in verify:
            print("1")
            return 1
        elif "Junior" in verify or "Junior Admin" in verify:
            print("2")
            return 2
        elif "Global" in verify or "Global Admin" in verify:
            print("3")
            return 3
        else:
            print("Error") 
    else:
        #print("User not found! ")
        user_not_found()

def session_UserSelection(username1):

    screen8 = Toplevel(screen)
    screen8.title("Raspberry Pi Deployment")
    screen8.geometry("300x300")
    Label(screen8,text = "Welcome to Raspberry Pi Deployment Server").pack()
    Label(screen8,text = "Please connect device to screen").pack()

    print(username1)
    print (ACL(username1))
    
    if ACL(username1) == 1:
        #User / Client 
        Button(screen8, text = "User / Client", width = 10, height = 1, command = user_admin).pack()
        Label(screen8,text = "").pack()
        Users = "User / Client"
        
    elif ACL(username1) == 2:
        #User / Client 
        Button(screen8, text = "User / Client", width = 10, height = 1, command = user_admin).pack()
        Label(screen8,text = "").pack()

        #Junior Admin
        Button(screen8, text = "Junior Admin", width = 10, height = 1, command = junior_admin).pack()
        Label(screen8,text = "").pack()

    elif ACL(username1) == 3:
        #User / Client 
        Button(screen8, text = "User / Client", width = 10, height = 1, command = user_admin).pack()
        Label(screen8,text = "").pack()

        #Junior Admin
        Button(screen8, text = "Junior Admin", width = 10, height = 1, command = junior_admin).pack()
        Label(screen8,text = "").pack()

        #Global Admin
        Button(screen8,text = "Global Admin", width = 10, height = 1, command = global_admin).pack()

    else:
        print("Error")
            
    #User / Client 
    #Button(screen8, text = "User / Client", width = 10, height = 1, command = user_admin).pack()
    #Label(screen8,text = "").pack()
    
    #Junior Admin
    #Button(screen8, text = "Junior Admin", width = 10, height = 1, command = junior_admin).pack()
    #Label(screen8,text = "").pack()
    
    #Global Admin
    #Button(screen8,text = "Global Admin", width = 10, height = 1, command = global_admin).pack()
    

def user_admin():

    global Users_Selected
    Users_Selected = "Standard"
   
    screen9 = Toplevel(screen)
    screen9.title("User / Client")
    screen9.geometry("400x400")
    Label(screen9, text="Welcome User").pack()
    Label(screen9, text="You are not required to do any changes to the device").pack()
    Button(screen9,text = "Launch", width = 10, height = 1, command = launch_machine).pack()
    Button(screen9,text = "Quit", width = 10, height = 1).pack()
    
def standardScript():
    global Users_Selected
    
    Users_Selected = "Standard"
    print (Users_Selected)

def liteScript():
    global Users_Selected
    
    Users_Selected = "Lite"
    print (Users_Selected)
   
def junior_admin():

    global Users_Selected
    
    screen10 = Toplevel(screen)
    screen10.title("Junior Admin")
    screen10.geometry("400x400")
    Label(screen10, text="Welcome Junior Admin").pack()
    Label(screen10,text = "", width = 10, height = 1).pack()

    #Junior Admin Buttons 
    Button(screen10,text = "Select Raspbian Lite", width = 20, height = 1, command = liteScript).pack()
    #Label(screen10,text = "", width = 10, height = 1).pack()
    Button(screen10,text = "Select Raspbian Normal", width = 20, height = 1, command = standardScript).pack()
    #Label(screen10,text = "", width = 10, height = 1).pack()
    Button(screen10,text = "Show all Devices", width = 20, height = 1).pack()
    #Label(screen10,text = "", width = 10, height = 1).pack()

    Button(screen10,text = "Launch", width = 20, height = 1, command = launch_machine).pack()
    Button(screen10,text = "Quit", width = 20, height = 1).pack()

def global_admin():

    global Users_Selected
    
    screen11 = Toplevel(screen)
    screen11.title("Global Admin")
    screen11.geometry("400x400")
    Label(screen11, text="Welcome Global Admin").pack()
    Label(screen11,text = "", width = 10, height = 1).pack()
    
    #Global Admin Buttons 
    Button(screen11,text = "Select Raspbian Lite", width = 20, height = 1, command = liteScript).pack()
    #Label(screen11,text = "", width = 10, height = 1).pack()
    Button(screen11,text = "Select Raspbian Normal", width = 20, height = 1, command = standardScript).pack()
    #Label(screen11,text = "", width = 10, height = 1).pack()
    Button(screen11,text = "Add New Device", width = 20, height = 1).pack()
    #Label(screen11,text = "", width = 10, height = 1).pack()
    Button(screen11,text = "Customise Configuration", width = 20, height = 1).pack()
    #Label(screen11,text = "", width = 10, height = 1).pack()
    
    Button(screen11,text = "Launch", width = 20, height = 1, command = launch_machine).pack()
    Button(screen11,text = "Quit", width = 20, height = 1).pack()

def launch_machine():

    global Users_Selected
    
    screen12 = Toplevel(screen)
    screen12.title("Deployment Launch")
    screen12.geometry("400x400")
    Label(screen12, text="Welcome Launch Area").pack()

    Label(screen12, text="Please wait for the reboot of the Server").pack()
    Label(screen12, text="Please turn on the device \n via power button to begin").pack()
    #Label(screen12, text="This will take approx 40 minutes to complete").pack()

    Button(screen12,text = "Launch", width = 20, height = 1, command = launchButton).pack()
    Button(screen12,text = "Quit", width = 20, height = 1).pack()
    

def launchButton():
    print (Users_Selected)
    if (Users_Selected == "Lite"):
        print("Code for Lite")
        os.system('./LiteScript')
    elif (Users_Selected == "Standard"):
        print("Code for Standard")
        os.system('./StandardScript')
    else:
        print("Error")
    
    



def login_success(username1):
    #global screen3
    #screen3 = Toplevel(screen)
    #screen3.title("Success")
    #screen3.geometry("150x100")
    #Label(screen3, text = "Login Successful").pack()
    #Button(screen3, text = "OK", command = delete2).pack()
    session_UserSelection(username1)
    
def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Password not recongised")
    screen4.geometry("150x100")
    Label(screen4, text = "Password Error").pack()
    Button(screen4, text = "OK", command = delete3).pack()
    
def user_not_found():
    #print("Working")
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("User not recongised")
    screen5.geometry("150x100")
    Label(screen5, text = "Username Error").pack()
    Button(screen5, text = "OK", command = delete4).pack()
    

def register_user():
    
    username_info = username.get()
    password_info = password.get()
    typeuser_info = typeuser.get()

    file=open(username_info,"w")
    file.write(username_info+"\n")
    file.write(password_info+ "\n")
    file.write(typeuser_info+ "\n")
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    typeuser_entry.delete(0, END)
    
    Label(screen1, text = "Registration Success", fg = "green", font = ("Calibri", 11)).pack()

def login_verify():
    #print("Working....")

    username1 = username_verify.get()
    password1 = password_verify.get()
    typeuser1 = typeuser_verify.get()

    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    #typeuser_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            print ("Login Success")
            login_success(username1)
        else:
            print("Password Failed")
            password_not_recognised()
    else:
        print("User not found! ")
        user_not_found()
        
def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("250x300")

    global username
    global password
    global typeuser
    
    global username_entry
    global password_entry
    global typeuser_entry
    
    username = StringVar()
    password = StringVar()
    typeuser = StringVar()

    Label(screen1, text = "Please enter your details below").pack()
    #Label(screen1, text = "").pack()
    Label(screen1, text = "Username * ").pack()

    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "Password * ").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text = "Type of User * ").pack()
    typeuser_entry = Entry(screen1, textvariable = typeuser)
    typeuser_entry.pack()

    Button(screen1, text="Register", width = 5, height = 1, command = register_user).pack()


def login():
   # print("Login Session Started")
   global screen2
   screen2 = Toplevel(screen)
   screen2.title("Login")
   screen2.geometry("300x350")

   Label(screen2, text = "Please enter your details below to login").pack()
   Label(screen2, text = "").pack()

   global username_verify
   global password_verify
   global typeuser_verify

   username_verify = StringVar()
   password_verify = StringVar()
   typeuser_verify = StringVar()

   global username_entry1
   global password_entry1
   global typeuser_entry1
   
   Label(screen2, text = "Username * ").pack()
   username_entry1 = Entry(screen2, textvariable = username_verify)
   username_entry1.pack()
   Label(screen2, text = "").pack()

   Label(screen2, text = "Password * ").pack()
   password_entry1 = Entry(screen2, textvariable = password_verify)
   password_entry1.pack()
 
   Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()

def main_screen():
    global screen
    screen=Tk()
    screen.geometry("300x250")
    screen.title("Raspberry Pi")

    Label(text="Raspberry Pi", bg = "grey", width = "150", height = "2", font = ("Calibri", 10)).pack()
    Label (text = "").pack()
    Button(text = "Login", height = "2", width = "15", command = login).pack()
    Label (text = "").pack()
    Button(text = "Register", height = "2", width = "15", command = register).pack()

    screen.mainloop()
main_screen()
    
        
