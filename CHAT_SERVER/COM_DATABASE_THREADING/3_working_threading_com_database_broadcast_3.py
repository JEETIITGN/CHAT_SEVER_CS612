import socket               # Import socket module
import threading
import MySQLdb
broadcastdb="BROADCAST_DATABASE"
broadcasttb="BROADCASTING_TABLE"
data=""

def Main():	
    server_first_flag='1'
    print "Server start flag = ",server_first_flag
    while 1:
        if server_first_flag=='1':
            setup()
            server_first_flag='0'
        else:
            print "Server start flag = ",server_first_flag
            s_send = socket.socket()         # Create a socket object
            s_rec = socket.socket()         # Create a socket object
            
            host = '10.1.136.114' # Get local machine name
            port_rec = 5001     # PORT FOR SERVER TO RECEIVE 
            port_send = 5000     # PORT FOR SERVER TO BRAODCAST

            print 'Server started!'
            # print 'Waiting for clients...'
            # print "jeet the great"
            s_send.bind((host, port_send))        # Bind to the port
            s_send.listen(5)                 # Now wait for client connection.
            
            s_rec.bind((host, port_rec))        # Bind to the port
            s_rec.listen(5)                 # Now wait for client connection.
            
            while True:
                c_send, addr_send = s_send.accept()     # Establish connection with client.
                c_rec, addr_rec = s_rec.accept()
                # print "The connection variable c is | ",c," and the address is | ",addr[0],addr[1]
                # print broadcastdb, "of type ",type(broadcastdb)
                # receiver(c_rec,addr_rec,c_send,addr_send)
                t1=threading.Thread(target=receiver,args=(c_rec,addr_rec,c_send,addr_send))
		        # thread.start_new_thread(broad_client,(cserv,addrserv))
                t1.start()
                # t1.join()
                print "Returned from Receiver function"
                # thread.start_new_thread(receiver,(c_rec,addr_rec,c_send,addr_send))
                # thread.start_new_thread(broadcast,(c,addr))
                #Note it's (addr,) not (addr) because second parameter is a tuple
                #Edit: (c,addr)
                #that's how you pass arguments to functions when creating new threads using thread module.
                # while 1:
                	# pass
            print "FINAL SOCKET CLOSURE"
            s.close()

def receiver(clientsocket,addr,c_send,addr_send):
	# while True:
    # delete_table()
    # exit()
    print "In receiver"
    db = MySQLdb.connect("Jeet.local","root","heythere",database=broadcastdb )
    cursor = db.cursor()
    sql="""SHOW DATABASES"""
    cursor.execute(sql)
    flag=0
    for dbs in cursor:
        # print dbs,"  " ,flag
        if broadcastdb in dbs:
            flag=1
    if flag==0:
        create_broadcast_database()
    else:
        print "NO NEED TO CALL CREATE_DATABASE"
    
    sql="""SHOW TABLES"""
    cursor.execute(sql)
    flag=0
    for dbs in cursor:
        print dbs,"  " ,flag
        if broadcasttb in dbs:
            flag=1
    if flag==0:
        create_broadcast_table()
    else:
        print "NO NEED TO CALL CREATE_TABLE"

    db.close()
    db=MySQLdb.connect("Jeet.local","root","heythere","BROADCAST_DATABASE")
    cursor=db.cursor()
    while 1:
        data = clientsocket.recv(1024)
        # call the logger function and sends this message to all the group members
        #do some checks and if msg == someWeirdSignal: break:
        if not data:
            print ("No dta received")
            break
        else:
            print addr, ' >> ', data
            try:
                # print "Trying to insert socket and ip into the database"
                sql="""SELECT * FROM BROADCASTING_TABLE WHERE IP IN ("%s")""" % (addr[0])
                cursor.execute(sql)
                result=cursor.fetchall()
                if len(result) == 0:
                    sql="""INSERT INTO BROADCASTING_TABLE (SOCKET,IP) VALUES ('%s','%s')""" % (clientsocket,addr[0]) # addr is not an string
                    # print "BEFORE EXEC"
                    cursor.execute(sql)
                    print "INSERTION"
                    db.commit()
                    sql=("SELECT * FROM BROADCASTING_TABLE")
                    try:
                        cursor.execute(sql)
                        result=cursor.fetchall()
                        # results =cursor.fetchall()
                        for df in result:
                            print df
                    except:
                        print "Unable to display the content of the table" 
                else:
                    print "IP already exists"           
            except:
                print "Unable to add the socket and the IP into the database"
            
            broadcast_message(c_send,addr_send)

            # broadcast(clientsocket,data)# make it to thread for sending the received data globally to all the group members
        # msg = raw_input('SERVER >> ')
        #Maybe some code to compute the last digit of PI, play game or anything else can go here and when you are done.
        # clientsocket.send(msg)
	print "Closing socket"    

    clientsocket.close()
def broadcast_message(clientsocket,addr):
    db=MySQLdb.connect("Jeet.local","root","heythere","BROADCAST_DATABASE")
    cursor=db.cursor()
    print "Inside broadcaster"
    sql="""SELECT * FROM BROADCASTING_TABLE WHERE IP NOT IN ('%s')""" % (addr[0])
    try:
        cursor.execute(sql)
        print "Broadcasting selection complete | "
        db.commit()
    except:
        print "Need more work in broadcaster"
        db.rollback()
    
    print "Displaying result" 
    result=cursor.fetchall()
    for res in result:
        print res
    clientsocket.send(data)
    db.close()
def setup():
    delete_database()
    create_broadcast_database()
    delete_table()
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
        sql = """CREATE TABLE BROADCASTING_TABLE (SOCKET CHAR(100) NOT NULL, IP CHAR(20) NOT NULL)"""#The created table have the second entry that is receiving the integer value but I am trying to throw in string value
        # print "Executing the table creation command to the database"
        cursor.execute(sql)
        # print "Finished Executing the table creation command to the database"
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
    print "ISPE FOCUS ",broadcastdb
    db = MySQLdb.connect("Jeet.local","root","heythere",database=broadcastdb)
    print ("Database creation successful with database descriptor: ", db)
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
        print "Deleting table"
        sql="""DROP TABLE BROADCASTING_TABLE"""
        cursor.execute(sql)
        print "Dropping completed"
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
