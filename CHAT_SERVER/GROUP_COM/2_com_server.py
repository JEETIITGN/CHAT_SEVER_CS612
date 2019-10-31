import socket               # Import socket module
import threading
import MySQLdb

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
            host = '10.1.136.114' # Get local machine name
            port_ctrl = 5000     # PORT FOR SERVER TO RECEIVE 
            
            s_ctrl.bind((host, port_ctrl))        # Bind to the port
            s_ctrl.listen(5) 
            print "Server CTRL Started"
            
            # s_data = socket.socket()         # Create a socket object
            # port_data = 5001     # PORT FOR SERVER TO RECEIVE 
            # print 'Waiting for clients...'
            # print "jeet the great"
            # s_data.bind((host, port_data))        # Bind to the port
            # s_data.listen(5)                 # Now wait for client connection.
            
            while True:
                c_ctrl, addr_ctrl = s_ctrl.accept()     # Establish connection with client.
                t1=threading.Thread(target=controller,args=(c_ctrl,addr_ctrl))
                t1.start()
            s.close()
socket_list=[]
def controller(clientsocket,addr):
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
            sign_in(clientsocket,addr)
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
    username = clientsocket.recv(1024)
    if not username:
        print ("No dta received")
    else:
        print addr, ' >> ', username
    # try:
        # print "Trying to insert into the database"
        sql="""SELECT * FROM BROADCASTING_TABLE WHERE USERNAME IN ("%s")""" % (username)
        cursor.execute(sql)
        result=cursor.fetchall()
        print result
        if len(result) == 0:
            print "USERNAME ",username, "DOES NOT EXIST ADDING TO THE DATABASE"
            passwd=clientsocket.recv(1024)
            print "USERNAME_CREATED"
            clientsocket.send("USERNAME_CREATED")
            print "WAITING FOR CHOICE OF GROUP | "
            choice=clientsocket.recv(1024)
            groupname=0
            if choice == '1':
                groupname=groupname + 1;
            elif choice == '2':
                groupname=groupname + 2*10;
            elif choice == '3':
                groupname=groupname + 3*100;
            elif choice == '4':
                groupname=groupname + 4*1000;
            elif choice == '5':
                groupname=groupname + 5*10000;
            print groupname
            sql="""INSERT INTO BROADCASTING_TABLE (USERNAME,PASSWORD,IP,GROUPNAME) VALUES ('%s','%s','%s','%d')""" % (username,passwd,addr[0],groupname) 
            try:
                cursor.execute(sql)
                print "ADDED ENTRY TO THE DATABASE"
                db.commit()
                
            except:
                print "UNABLE TO ADD TO THE DATABASE"
                db.rollback()
        else:
            print "USERNAME ",username," EXIST"  
            clientsocket.send("ERROR")
              

def sign_in(clientsocket,addr):
    db = MySQLdb.connect("Jeet.local","root","heythere",database=broadcastdb )
    cursor = db.cursor()
    # while 1:#NEED?
    # clientsocket.send("OK")
    username = clientsocket.recv(1024)
    print "USERNAME RECEIVED | ",username
    # call the logger function and sends this message to all the group members
    #do some checks and if msg == someWeirdSignal: break:
    if not username:
        print ("No dta received")
    else:
        print addr, ' >> ', username
    # try:
        print "Trying to insert into the database"
        sql="""SELECT * FROM BROADCASTING_TABLE WHERE USERNAME IN ("%s")""" % (username)
        cursor.execute(sql)
        result=cursor.fetchall()
        # print result[0]
        # print result[0][0]
        # exit()
        if len(result) == 0:
            print "USERNAME ",username, "DOES NOT EXIST"
            clientsocket.send("ERROR")
        else:
            print "USERNAME ",username," EXIST"  
            clientsocket.send("EXIST")
            passwd=clientsocket.recv(1024)
            if passwd == result[0][1]:
                clientsocket.send("PASSWD-CORRECT")
                socket_list.append(clientsocket)
                print "sending groups"
                clientsocket.send(str(result[0][3]))
                sign_in_screen(clientsocket,addr)
            else:
                clientsocket.send("PASSWD-INCORRECT")
# def sign_in_group(clientsocket,addr):
#     db = MySQLdb.connect("Jeet.local","root","heythere",database=broadcastdb )
#     cursor = db.cursor()
#     sql="""SELECT * FROM BROADCASTING_TABLE WHERE """
#     db.close()
def sign_in_screen(clientsocket,addr):
    message=clientsocket.recv(1024)
    if message == "CHAT":
        receiver(clientsocket,addr)













def receiver(clientsocket,addr):
    # print "In receiver"
    db = MySQLdb.connect("Jeet.local","root","heythere",database=broadcastdb )
    cursor = db.cursor()
    while 1:
        message = clientsocket.recv(1024)
        if not message:
            print ("No dta received")
            break
        elif message == "QUIT":
            # Main()
        else:
            print addr, ' >> ', data
            s_data = socket.socket()         # Create a socket object
            host = '10.1.136.114' # Get local machine name
            port_data = 5001     # PORT FOR SERVER TO RECEIVE 
            s_data.bind((host, port_data))        # Bind to the port
            s_data.listen(5) 
            print "Server CTRL Started"
            c_data, addr_data = s_data.accept()     # Establish connection with client.
            message=s_data.recv(1024)
            len_list=len(socket_list)
            for cs in socket_list: 
                # print 
                print ""
                if cs != c_send:
                    print "Clientsocket: ",cs, "  msg | ",msg
                    cs.send(msg)
                else:
                    print "MATCH NOT SENDING TO THE SENDER"
        


            # t1=threading.Thread(target=broadcast_message,args=(clientsocket,addr,c_data,addr_data))
            # t1.start()
            # s.close()

            # (socket_list,data,addr_send,c_send)
            # try:   
                # print "Trying to insert socket and ip into the database"
            #     sql="""SELECT * FROM BROADCASTING_TABLE WHERE USERNAME IN ("%s")""" % (data)
            #     cursor.execute(sql)
            #     result=cursor.fetchall()
            #     if len(result) == 0:
            #         sql="""INSERT INTO BROADCASTING_TABLE (SOCKET,IP) VALUES ('%s','%s')""" % (c_send,addr_send[0]) # addr is not an string
            #         # print "BEFORE EXEC"
            #         cursor.execute(sql)
            #         # print "INSERTION"
            #         db.commit()
            #         print "Socket list before | ",socket_list
            #         socket_list.append(c_send)
            #         print "Socket list after | ",socket_list
            #         sql=("SELECT * FROM BROADCASTING_TABLE")
            #         try:
            #             cursor.execute(sql)
            #             result=cursor.fetchall()
            #             # results =cursor.fetchall()
            #             # for df in result:
            #                 # print df
            #         except:
            #             print "Unable to display the content of the table" 
            #     else:
            #         print "IP already exists"           
            # except:
            #     print "Unable to add the socket and the IP into the database"
            # # clientsocket.send(data)
            # broadcast_message(socket_list,data,addr_send,c_send)

            # broadcast(clientsocket,dat
            # a)# make it to thread for sending the received data globally to all the group members
        # msg = raw_input('SERVER >> ')
        #Maybe some code to compute the last digit of PI, play game or anything else can go here and when you are done.
        # clientsocket.send(msg)
	print "Closing socket"    

    clientsocket.close()
def broadcast_message(clientsocket,addr,c_data,addr_data):
    # db=MySQLdb.connect("Jeet.local","root","heythere","BROADCAST_DATABASE")
    # cursor=db.cursor()
    # # print "Inside broadcaster"
    # sql="""SELECT * FROM BROADCASTING_TABLE WHERE IP NOT IN ('%s')""" % (addr[0])
    # try:
    #     cursor.execute(sql)
    #     # print "Broadcasting selection complete | "
    #     db.commit()
    # except:
    #     print "Need more work in broadcaster"
    #     db.rollback()
    
    # result=cursor.fetchall()
    
    # print "Displaying result" 
    # result=cursor.fetchall()
    # # print "The list that can save me | ",socket_list
    message=
    len_list=len(socket_list)
    for cs in socket_list: 
        print cs,
        print ""
        if cs != c_send:
            print "Clientsocket: ",cs, "  msg | ",msg
            cs.send(msg)
        else:
            print "MATCH NOT SENDING TO THE SENDER"
        


    print "sent data | ",msg

    # sql="""SELECT* FROM BROADCASTING_TABLE WHERE """
    # clientsocket.send(msg)

    db.close()
def setup():
    delete_database()
    create_broadcast_database()
    # delete_table()
    create_broadcast_table()

def broadcast(clientsocket,data):
	# print msg
	if data !='':
		print "sendind data :" + str(data)
		clientsocket.send(str(data))
		# break
	# clientsocket.close()

def create_broadcast_database():
    # delete_table()

    db=MySQLdb.connect("Jeet.local","root","heythere")
    cursor=db.cursor()
    try:
        sql="""CREATE DATABASE BROADCAST_DATABASE"""
        cursor.execute(sql)
        db.commit()
    except:
        print "DATABASE ",broadcastdb, " is already created."
        db.rollback()
    print "LISTING DATABASES"
    cursor.execute("SHOW DATABASES")
    for dbs in cursor:
        print dbs
    print ""
    # print "Trying to create the table named BROADCASTING_TABLE"
    db.close()
def create_broadcast_table():

    db=MySQLdb.connect("Jeet.local","root","heythere",database=broadcastdb)
    cursor=db.cursor()
    try:
        # print "Defining variable sql to write to the database"
        # delete_table()
        sql = """CREATE TABLE BROADCASTING_TABLE ( USERNAME CHAR(100) NOT NULL, PASSWORD CHAR(100) NOT NULL, IP CHAR(20) NOT NULL, GROUPNAME INT )"""
        print "Executing the table creation command to the database"
        cursor.execute(sql)
        print "Finished Executindg the table creation command to the database"
        # print "LISTING TABLES after table creation "
        cursor.execute("""SHOW TABLES""")
        for tbs in cursor:
            print tbs
        db.commit() #db is the file descriptor for our database commit would write the changes
    except:
        print "Table already created"
        db.rollback()#rollback would undo the cursor.execute(sql) command
    # print "LISTING TABLES"
    cursor.execute("""SHOW TABLES""")
    for tbs in cursor:
        print tbs
    # exit()
    
    db.close()
    
def delete_database():
    # print "ISPE FOCUS ",broadcastdb
    db = MySQLdb.connect("Jeet.local","root","heythere",database=broadcastdb)
    # print ("Database creation successful with database descriptor: ", db)
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    sql="SHOW TABLES"
    cursor.execute(sql)

    try:
        # print "Trying to insert values to the tables"
        print "Deleting database"
        sql="""DROP DATABASE BROADCAST_DATABASE"""
        cursor.execute(sql)
        db.commit()
    except:
        print "Unable to drop database"
        db.rollback()
    cursor.execute("SHOW DATABASES")
    print ""
    for dbs in cursor:
        print dbs
    print ""
    db.close()

def delete_table():
    db = MySQLdb.connect("Jeet.local","root","heythere","BROADCAST_DATABASE" )
    # print ("Database creation successful with database descriptor: ", db)
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # print "Done creating database cursor"
    try:
        # print "Deleting table"
        sql="""DROP TABLE BROADCASTING_TABLE"""
        cursor.execute(sql)
        # print "Dropping completed"
        db.commit()
        cursor.execute("SHOW TABLES")
        for cu in cursor:
            print cu
    except:
        print "Unable to delete the table"
        db.rollback()
    db.close()
if __name__ == '__main__':
	Main()
