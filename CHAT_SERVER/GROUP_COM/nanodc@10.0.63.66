import socket               # Import socket module
import threading
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
        choice= raw_input("Enter you choice | ")

        if choice == '1':
            sign_in()
        elif choice == '2':
            sign_UP()
        else:
            exit()

username=""
def sign_in():
    print "MENU FOR SIGNING IN"
    message="sign_in"
    s_ctrl.send(message)
    
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
    groupname=raw_input("ENTER YOUR CHOICE | ")
    print "Sending ",groupname
    s_ctrl.send(str(groupname))
    sign_in_pass(groupname)
    Main()
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
    print "SIGN IN SUCCESSFULLY"
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
        chatting(group_name)
    elif choice == "1":
        message="ls"
        s_ctrl.send(message)

    elif choice == "2":
        message="UPLOAD"
        s_ctrl.send(message)

    elif choice == "3":
        message="DOWNLOAD"
        s_ctrl.send(message)

    elif choice == "4":
        message="rm"
        s_ctrl.send(message)

    elif choice == "5":
        message="SHARE"
        s_ctrl.send(message)

    elif choice == "6":
        message="DISP_LOG"
        s_ctrl.send(message)

    elif choice == "7":
        print "Signing Out"
        message="SIGN_OUT"
        s_ctrl.send(message)

    else: 
        Main()
    # print "Sending | ",message
    # s_ctrl.close()
    print "REQUEST SENT"
    # data = s_ctrl.recv(1024)
    # print data

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
        message = serversocket.recv(1024)
        if message == "QUIT":
            sign_in_pass(groupname)
        print "DATA RECEIVED | ",message
    print "Exiting from receive"
    serversocket.close()

def send(serversocket,groupname):
    print "Inside send message block"
    while True:
        message = raw_input(" ->")
        if message=="QUIT":
            sign_in_pass(groupname)
        print "Sending | ",message
        serversocket.send(message)
    print "Out of infinite loop in send-client"
    serversocket.close()


if __name__ == '__main__':
	Main()
