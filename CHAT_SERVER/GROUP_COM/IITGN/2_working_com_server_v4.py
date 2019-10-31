import socket               # Import socket module
import threading
import MySQLdb
import os

group_list=["IITGN","ENGINEERING","MATLAB","PYTHON","ENTREPRENEUR"]

broadcastdb="BROADCAST_DATABASE"
broadcasttb="BROADCASTING_TABLE"
data=""
def Main():	
    server_first_flag='1'
    # print "Server start flag = ",server_first_flag
    while 1:
        if server_first_flag=='1':
            setup()
            server_first_flag='0'
        else:
            # print "Server start flag = ",server_first_flag
            # s_send = socket.socket()         # Create a socket object
            s_ctrl = socket.socket()         # Create a socket object
            s_data = socket.socket()
            host = '10.1.136.114' # Get local machine name
            port_ctrl = 5000     # PORT FOR SERVER TO RECEIVE 
            port_data = 5001
            s_ctrl.bind((host, port_ctrl))        # Bind to the port
            s_data.bind((host,port_data))
            s_ctrl.listen(5) 
            s_data.listen(5)
            print "Server CTRL Started"
            
            # s_data = socket.socket()         # Create a socket object
            # port_data = 5001     # PORT FOR SERVER TO RECEIVE 
            # print 'Waiting for clients...'
            # print "jeet the great"
            # s_data.bind((host, port_data))        # Bind to the port
            # s_data.listen(5)                 # Now wait for client connection.
            
            while True:
                c_ctrl, addr_ctrl = s_ctrl.accept()     # Establish connection with client.
                c_data, addr_data = s_data.accept()     # Establish connection with client.
                print c_ctrl,"  ",c_data
                t1=threading.Thread(target=controller,args=(c_ctrl,addr_ctrl,c_data,addr_data))
                t1.start()
            s.close()

socket_list_group_1=[]
socket_list_group_2=[]
socket_list_group_3=[]
socket_list_group_4=[]
socket_list_group_5=[]

def controller(clientsocket,addr,clientdatasocket,addr_data):
    print "Inside reply message block"
    while True:
        print "CLIENT IN FIRST_SCREEN|"
        message = clientsocket.recv(1024)
        print str(message)
        if not message:
	        break
        if message == "sign_in":
            print "inside sign_in_block"
            clientsocket.send("OK")
            sign_in(clientsocket,addr,clientdatasocket,addr_data)
        elif message == "sign_up":
            print "inside sign-up block"
            clientsocket.send("OK")
            sign_up(clientsocket,addr)
        else:
            print "Improve your controller"
        print "Back in controller +  closing socket"
        # clientsocket.close()
    print "Outside while"
        # msg = raw_input('SERVER >> ')
        #Maybe some code to compute the last digit of PI, play game or anything else can go here and when you are done.
        # clientsocket.send(msg)
    # clientsocket.close()

def sign_up(clientsocket,addr):
    db = MySQLdb.connect("Jeet.local","root","heythere",database=broadcastdb )
    cursor = db.cursor()
 