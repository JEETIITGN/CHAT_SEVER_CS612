import socket               # Import socket module
import threading
import os
import sys
# import MySQLdb
# import first_screen
s_ctrl = socket.socket()         # Create a socket object
s_data = socket.socket()
host = '10.1.136.114' # Get local machine name
port_ctrl = 5000     # PORT FOR SERVER TO RECEIVE 
port_data = 5001
s_ctrl.connect((host, port_ctrl))        # Bind to the port
s_data.connect((host,port_data))
print "Connected with server-ctrl"
# broadcastdb="CHAT_SERVER_DATABASE"
# broadcasttb="CHAT_SERVER"
group_list=["IITGN","ENGINEERING","MATLAB","PYTHON","ENTREPRENEUR"]
message=""

def Main():	
    # setup()
    print "Welcome to the CHAT_SERVER_BETA_VERSION."
    while 1:
        print "Press 1: Sign_IN"
        print "Press 2: Sign_UP"
        # print "Press 5: ADMIN-LOGIN"
        print "Any other to EXIT"
        try:
            choice= raw_input("Enter you choice | ")
        except:
            print "SHUTTING DOWN"
            
        if choice == '1':
            sign_in()
        elif choice == '2':
            sign_UP()
        else:
            s_ctrl.close()
            s_data.close()
            exit()

username=""
def sign_in():
    print "MENU FOR SIGNING IN"
    message="sign_in"
    try:
        s_ctrl.send(message)
    except:
        print "EXITING "
    try:
        message=s_ctrl.recv(1024)
        print message
        if message == "OK":
            try:
                # print "Inside try block in sign_in"
                print "WAITING FOR SERVER TO CONNECT"
                username=raw_input("USERNAME | ")
                s_ctrl.send(username)
                # s_ctrl.close()
                # username=message
                data = s_ctrl.recv(1024)
                print "received data ",data
                if data == "EXIST":
                    message=raw_input("PASSWORD | ")
                    s_ctrl.send(message)
                    # s_ctrl.close()
                    data = s_ctrl.recv(1024)
                    print data
                    if data == "PASSWD-CORRECT":
                        print "SIGNING-IN"
                        s_ctrl.send("SIGNED_IN")
                        sign_in_group() #FOCUS HERE
                    elif data == "PASSWD-INCORRECT":
                        print "INCORRECT PASSWORD"
                        Main()
                    else:
                        print "SIGN_IN NEEDS IMPROVEMENT"

                elif data == "ERROR":
                    print "USERNAME DOES NOT EXIST"
                    Main()
            except:
                print "SIGN_IN MODULES HAVE SOME ERRORS"
        else:
            print "NOT RECEIVED OK"
    except:
        print "EXITING-APPLICATION"
        exit()
def sign_in_group():
    print "SELECT THE GROUP TO ENTER|"
    message=s_ctrl.recv(1024)#focus
    groups=int(message)
    print "GROUPS | ",groups
    i=0
    print "YOU HAVE SIGNED-UP FOR THE FOLLOWING GROUPS| PLEASE TYPE THE GROOUP NAME TO ENTER|"
    if groups%10 == 1:
        i=i+1
        print "| IITGN"
        # message=("IIT-GN")
    groups=groups/10

    if groups%10 == 2:
        i=i+1
        print "| ENGINEERING"
        # message=("ENGINEERING")
    groups=groups/10

    if groups%10 == 3:
        i=i+1
        print "| MATLAB"
        # message=("MATLAB")
    groups=groups/10

    if groups%10 == 4:
        i=i+1
        print "| PYTHON"
        # message=("PYTHON")
    groups=groups/10

    if groups%10 == 5:
        i=i+1
        print "| ENTREPRENEUR"
        # message=("ENTREPRENEUR")
    groups=groups/10

    print ""
    print "OR"
    print ""

    print "Press 1 | JOIN GROUP "
    print "Press 2 | LEAVE GROUP "
    # print "Press 3 | LIST GROUP "

    groupname=raw_input("ENTER YOUR CHOICE | ")
    print "Sending ",groupname
    s_ctrl.send(str(groupname))
    if groupname == '1' or groupname == '2':
        print "GROUP_SIGN_UP"
        sign_up_group(groupname)
    elif groupname in group_list:
        sign_in_pass(groupname)
        Main()
    else:
        print "INVALID GROUP NAME "
        Main()
def sign_up_group(groupname):
    if groupname == "1":
        print "JOIN GROUP"
        sign_up_pass()
    elif groupname == "2":
        print "LEAVE GROUP"
        sign_up_pass()
    else:
        print "INVALID OPTION"
        # print 
def sign_UP():
    print "MENU FOR SIGNING UP"
    message="sign_up"
    s_ctrl.send(message)
    try:
        print "Inside try block in sign_up"
        print "Checking if username exists"
        username=raw_input("USERNAME | ")
        s_ctrl.send(username)
        data = s_ctrl.recv(1024)

        if data == "OK":
            passwd=raw_input("PASSWORD | ")
            s_ctrl.send(passwd)
            message = s_ctrl.recv(1024)
            print "USERNAME Wala message | ",message
            if message == "USERNAME_CREATED":
                print "SIGNING-UP"
                sign_up_pass()
            elif message == "ERROR":
                print "USERNAME ALREADY EXISTS RETURNING TO MAIN "
                Main()
        else:
            print "SIGN-UP UNSUCCESSFUL RETURNING TO MAIN "
            Main()
            
    except:
        print "SIGN_UP MODULES HAVE SOME ERRORS"

def sign_up_pass():
    i=0
    print "SIGN_UP_PASS"
    for group_name in group_list:
        print ""
        print "Press ",i+1," | ",group_name
        i=i+1
        print ""
    message=raw_input("ENTER YOUR CHOICE | ")
    s_ctrl.send(message)
    # s_ctrl.close()
    print "REQUEST SENT"
    # data = s_ctrl.recv(1024)
    # print data

def sign_in_pass(group_name):
    print "SIGN IN WIZARD"
    print "Press 0: Chatting"
    print "Press 1: List files"
    print "Press 2: Upload files"
    print "Press 3: Download files"
    print "Press 4: Delete files"
    print "Press 5: Share files"
    print "Press 6: Show log"
    print "Press 7: Sign out"
    choice= raw_input("Enter your choice | ")
    if choice == "0":
        message="CHAT"
        s_ctrl.send(message)
        print "Press 1 | View previous chat "
        print "Press 2 | Realtime chat window"
        choice=raw_input("Enter your choice | ")
        s_ctrl.send(choice)

        if choice == '1':
            print "SHOW LOG"
            show_log(group_name)
            sign_in_pass(group_name)
        elif choice == '2':
            print "CHATTING WINDOW"
            chatting(group_name)
        else:
            print "INVALID CHOICE"
            sign_in_pass(group_name)
            
    elif choice == "1":
        message="ls"
        s_ctrl.send(message)
        message=s_ctrl.recv(1024)
        ls=message.split("-")
        # print ""
        print "LIST OF THE DIRECTORY  |",group_name, " | ",ls
        sign_in_pass(group_name)
    elif choice == "2":
        message="UPLOAD"
        s_ctrl.send(message)
        upload_wizard()
        sign_in_pass(group_name)
    elif choice == "3":
        message="DOWNLOAD"
        s_ctrl.send(message)
        sys.stdout.flush()
        download_wizard(group_name)
        sign_in_pass(group_name)
    elif choice == "4":
        message="rm"
        s_ctrl.send(message)

        message=s_ctrl.recv(1024)
        ls=message.split("-")
        # print ""
        print "LIST OF THE DIRECTORY  |",group_name, " | ",ls

        message=raw_input("ENTER THE FILENAME TO REMOVE | ")
        s_ctrl.send(message)
        status=s_ctrl.recv(1024)
        if status == "RM_SUCCESS":
            print "FILE | ",message," SUCCESSFULLY REMOVED"
        elif status == "RM_FAILED":
            print "FILE | ",message," COULD NOT BE REMOVED"
        else:
            print "THERE IS SOME ERROR IN REMOVING FILE PLEASE CONTACT YOUR ADMINISTRATOR"
        sign_in_pass(group_name)
    elif choice == "5":
        message="SHARE"
        s_ctrl.send(message)
        message=s_ctrl.recv(1024)
        if message == "READY_TO_SHARE":
            sharing_wizard()
        sign_in_pass(group_name)
        #SIMLINKS---> 
    elif choice == "6":
        message="cat"
        s_ctrl.send(message)
        show_log(group_name)
        sign_in_pass(group_name)
    elif choice == "7":
        print "Signing Out"
        message="SIGN_OUT"
        s_ctrl.send(message)
        Main()
    else: 
        Main()
    # print "Sending | ",message
    # s_ctrl.close()
    print "REQUEST SENT"
    # data = s_ctrl.recv(1024)
    # print data

def show_log(group_name):
    print "SHOWING LOG FILE | "
    
    log_file_size=s_ctrl.recv(1024)
    print "LOG FILE SIZE | ",log_file_size,s_data
    kBtoRecv=s_data.recv(1024)
    print kBtoRecv
    totRecv=len(kBtoRecv)
    while str(totRecv) < log_file_size:
        kBtoRecv=s_data.recv(1024)
        print kBtoReceive
        totRecv+=len(kBtoRecv)
    print "END OF FILE"

def upload_wizard():
    print "UPLOAD_WIZARD"
    for dirpath,dirnames,filesnames in os.walk(os.getcwd()):
        if dirpath == os.getcwd():
            # print dirpath
            print filesnames
    filename = raw_input("FILENAME TO UPLOAD | ")
    
    if os.path.isfile(filename):
        print "FILE EXIST WAITING FOR SERVER TO RECEIVE"
        filesize = os.path.getsize(filename)
        print filename,filesize
        s_ctrl.send(filename)
        print "waiting to receive"
        message=s_ctrl.recv(1024)
        print "Received message | ",message
        if message == "READY_TO_RECEIVE":
            print "SERVER READY TO RECEIVE FILE | ",filesize
            s_ctrl.send(str(filesize))
            # s_ctrl.send(filesize) #
            print "File to upload | ",filename
            with open (filename,'rb') as f:
                print "Sending first kB"
                kBtoSend=f.read(1024)
                print "Sent | ",kBtoSend
                s_data.send(kBtoSend)
                while kBtoSend !="":
                    kBtoSend=f.read(1024)
                    s_data.send(kBtoSend)
                print "FILE SENT SUCCESSFULLY"
        else:
            print "SERVER ERROR RETURNING TO MAIN"
    else:
        print "FILE | ",filename," DOES NOT EXIST"
        s_ctrl.send("ERR")
        upload_wizard()
        

def download_wizard(group_name):
    print "DOWNLOAD WIZARD"

    message=s_ctrl.recv(1024)
    ls=message.split("-")
    print "LIST OF THE DIRECTORY  |",group_name, " | ",ls

    filename = raw_input("FILE TO DOWNLOAD | ")
    s_ctrl.send(filename)
    status=s_ctrl.recv(1024)
    print "STATUS OF FILE | ",status,status[:5]
    if status[:5] == "EXIST":
        print "FILE EXIST"
        s_ctrl.send("OK")
        filesize=long(status[5:])
        print group_name,os.getcwd()
        dir_name=os.path.join(os.getcwd(),"CLIENT_"+group_name)
        print "trying to make directory | ",dir_name
        try:
            os.makedirs(str(dir_name))
        except:
            print "DIRECTORY ALREADY CREATED"
        file_name=os.path.join(dir_name,filename)
        print file_name
        f=open(file_name,'wb')
        print "File Open"
        kBtoReceive=s_data.recv(1024)
        f.write(kBtoReceive)
        print "Received File | ",kBtoReceive
        totRecv=len(kBtoReceive)
        print ""

        while totRecv < filesize:
                kBtoReceive=s_data.recv(1024)
                print "Received File | ",kBtoReceive
                totRecv += len(kBtoReceive)
                f.write(kBtoReceive)
        print "Download Complete"
        f.close()
    elif status == "DOES_NOT_EXIST":
        print "FILE DOES NOT EXIST"

    else:
        print "ENTERED IN DUMP"


def sharing_wizard():
    print "SHARING WIZARD | "
    filename=raw_input("FILENAME TO SHARE | ")
    s_ctrl.send(filename)
    message=s_ctrl.recv(1024)
    if message == "OK":
        i=0
        for group_name in group_list:
            print ""
            print "Press ",i+1," | ",group_name
            i=i+1
            print ""
        message=raw_input("ENTER YOUR CHOICE | ")
        s_ctrl.send(message)
    elif message == "FILE_DOES_NOT_EXIST":
        print "FILE | ",filename," DOES NOT EXIST"

def chatting(groupname):
    # s_data = socket.socket()         # Create a socket object
    # port_data = 5001     # PORT FOR SERVER TO BRAODCAST
    # s_dat.bind((host, port_data))        # Bind to the port
    # s_data.listen(5)                 # Now wait for client connection.
    while True:
        print "Inside while message block"
        #receive(s)
        t1=threading.Thread(target=send,args=(s_data,groupname))
        t2=threading.Thread(target=receive,args=(s_data,groupname))
        print "Starting thread T1"
        t1.start()
        print "Starting thread T2"
        t2.start()
        print "Joining thread T1 with the main()"
        t1.join()
        print "Joining thread T2 with the main()"
        t2.join()
    s_data.close()

def receive(serversocket,groupname):
    print "Inside receive message block"
    while True:
        print "Ready to receive data | "
        sys.stdout.flush()
        message = serversocket.recv(1024)
        if message == ":q":
            serversocket.send(":q")
            sign_in_pass(groupname)
        print "DATA RECEIVED | ",message
    print "Exiting from receive"
    serversocket.close()

def send(serversocket,groupname):
    print "Inside send message block"
    while True:
        message = raw_input(" ->")
        if message==":q":
            serversocket.send(":q")
            sign_in_pass(groupname)
        print "Sending | ",message
        sys.stdout.flush()
        serversocket.send(message)
    print "Out of infinite loop in send-client"
    serversocket.close()


if __name__ == '__main__':
	Main()
