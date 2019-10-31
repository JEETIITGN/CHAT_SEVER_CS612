import socket               # Import socket module
import threading
# import MySQLdb
# import first_screen
s_ctrl = socket.socket()         # Create a socket object
host = '10.1.136.114' # Get local machine name
port_ctrl = 5000     # PORT FOR SERVER TO RECEIVE 
s_ctrl.bind((host, port_ctrl))        # Bind to the port
s_ctrl.listen(5)                 # Now wait for client connection.
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
        elif choice == '5':
            admin()
        else:
            exit()

username=""
def sign_in():
    print "MENU FOR SIGNING IN"
    try:
        # print "Inside try block in sign_in"
        print "WAITING FOR SERVER TO CONNECT"
        c_ctrl, addr_ctrl = s_ctrl.accept()     # Establish connection with client.
        message=raw_input("USERNAME | ")
        s_ctrl.send(message)
        s_ctrl.close()
        username=message
        data = s_ctrl.recv(1024)

        if data == 'OK':
            message=raw_input("PASSWORD | ")
            s_ctrl.send(message)
            s_ctrl.close()
            data = s_ctrl.recv(1024)
            if data == 'OK':
                print "SIGNING-IN"
                sign_in_pass()
            else:
                print "INCORRECT PASSWORD"
                Main()
        else:
            print "USERNAME DOES NOT EXIST"
            Main()
    except:
        print "SIGN_IN MODULES HAVE SOME ERRORS"

def sign_UP():
    print "Inside play with database"

    try:
        print "Inside try block in sign_up"
        print "Checking if username exists"
        c_ctrl, addr_ctrl = s_ctrl.accept()     # Establish connection with client.
        message=raw_input("USERNAME | ")
        s_ctrl.send(message)
        s_ctrl.close()
        username=message
        data = s_ctrl.recv(1024)

        if data == 'OK':
            message=raw_input("PASSWORD | ")
            s_ctrl.send(message)
            s_ctrl.close()
            data = s_ctrl.recv(1024)
            if data == 'OK':
                print "SIGNING-UP"
                sign_up_pass()
            else:
                print "INCORRECT PASSWORD"
                Main()
        else:
            print "USERNAME EXIST"
            Main()
    except:
        print "SIGN_UP MODULES HAVE SOME ERRORS"

def sign_up_pass():

    print "GROUP CHOOSING WIZARD"
    i=0
    for group_name in group_list:
        print ""
        print "Press ",i," | ",group_name
        i++
        print ""
    choice=raw_input("ENTER YOUR CHOICE | ")
    s_ctrl.send(choice)
    s_ctrl.close()
    print "REQUEST SENT"
    data = s_ctrl.recv(1024)
    print data

# def admin():
#     print "Enter the ADMIN password | "
#     password=raw_input("PAssword | ")
#     if password=="heythere":

#         print "WELCOME JEET TO THE UNDERWORLD"
#         print "Press 1: DELETE TABLES"
#         print "Press 2: DELETE DATABASE"
#         print "Any other key to return to main menu"
#         choice = raw_input("Enter your choice | ")

#         if choice == '1':
#             delete_table()
#         elif choice == '2':
#             delete_database()
#         else :
#             Main()
#     else:
#         print "Incorrect password, returning to the main menu"
#         Main()

def sign_in_pass():
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
    if choice == '0':
        chatting()
    if choice == '1':
        message="ls"
    elif choice == '2':
        message="UPLOAD"
    elif choice == '3':
        message="DOWNLOAD"
    elif choice == '4':
        message="rm"
    elif choice == '5':
        message="SHARE"
    elif choice == '6':
        message="DISP_LOG"
    elif choice == '7':
        print "Signing Out"
        message="SIGN_OUT"
    else: 
        Main()
    s_ctrl.send(message)
    s_ctrl.close()
    print "REQUEST SENT"
    data = s_ctrl.recv(1024)
    print data

def chatting():
    s_data = socket.socket()         # Create a socket object
    port_data = 5001     # PORT FOR SERVER TO BRAODCAST
    s_dat.bind((host, port_data))        # Bind to the port
    s_data.listen(5)                 # Now wait for client connection.
    while message != 'quit':
        print "Inside while message block"
        #receive(s)
        t1=threading.Thread(target=send,args=(s_data,))
        t2=threading.Thread(target=receive,args=(s_data,))
        print "Starting thread T1"
        t1.start()
        print "Starting thread T2"
        t2.start()
        print "Joining thread T1 with the main()"
        t1.join()
        print "Joining thread T2 with the main()"
        t2.join()
    s_data.close()

def receive(clientsocket):
    print "Inside receive message block"
    while True:
        print "Ready to receive data | "
        message = clientsocket.recv(1024)
	    # print "Data received"
	    # if not message:
        #     print "No data"
        #     break
        # else:
        print "DATA RECEIVED | ",message
    print "Exiting from receive"
    clientsocket.close()

def send(clientsocket):
    print "Inside send message block"
    while True:
        message = raw_input(" ->")
        if message=="q":
            break
	    clientsocket.send(message)
    clientsocket.close()


if __name__ == '__main__':
	Main()
