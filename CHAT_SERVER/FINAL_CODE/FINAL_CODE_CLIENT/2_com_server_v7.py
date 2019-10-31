import socket               # Import socket module
import threading
import MySQLdb
import os
import time

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
                print c_ctrl,"  ",c_data
                c_ctrl, addr_ctrl = s_ctrl.accept()     # Establish connection with client.
                c_data, addr_data = s_data.accept()     # Establish connection with client.
                
                t1=threading.Thread(target=controller,args=(c_ctrl,addr_ctrl,c_data,addr_data))
                t1.start()
                print "In Main"
            s.close()

socket_list_group_1=[]
socket_list_group_2=[]
socket_list_group_3=[]
socket_list_group_4=[]
socket_list_group_5=[]

def controller(clientsocket,addr,clientdatasocket,addr_data):
    # print "Inside reply message block"
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
            # clientsocket.send("OK")
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
            clientsocket.send("OK")
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
    db.close()

# def leave_group()
def sign_in(clientsocket,addr,clientdatasocket,addr_data):
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
            controller(clientsocket, addr, clientdatasocket, addr_data)
        else:
            print "USERNAME ",username," EXIST"  
            clientsocket.send("EXIST")
            passwd=clientsocket.recv(1024)
            if passwd == result[0][1]:
                clientsocket.send("PASSWD-CORRECT")
                groupnames=result[0][3]
                dump=clientsocket.recv(1024) #receives SIGNED_IN
                temp=groupnames
                print temp
                print ""
                if temp%10 == 1:
                    socket_list_group_1.append(clientdatasocket)
                    print "Socket Group List 1 | ",socket_list_group_1
                temp=temp/10
                print temp
                print ""
                if temp%10 == 2:
                    socket_list_group_2.append(clientdatasocket)
                    print "Socket Group List 2 | ",socket_list_group_2
                temp=temp/10
                print temp
                print ""
                if temp%10 == 3:
                    socket_list_group_3.append(clientdatasocket)
                    print "Socket Group List 3 | ",socket_list_group_3
                temp=temp/10
                if temp%10 == 4:
                    socket_list_group_4.append(clientdatasocket)
                    print "Socket Group List 4 | ",socket_list_group_4
                temp=temp/10
                print temp
                print ""
                if temp%10 == 5:
                    socket_list_group_5.append(clientdatasocket)
                    print "Socket Group List 5 | ",socket_list_group_5
                
                print "Group names | ",result[0][3]
                # socket_list.append(clientdatasocket)
                print "sending groups"
                clientsocket.send(str(result[0][3]))
                groupname=clientsocket.recv(1024)
                if groupname == '1' or groupname == '2':
                    print "GROUP_SIGN_UP"
                    sign_up_group(clientsocket,addr,clientdatasocket,addr_data,groupname,username,groupnames)
                elif groupname in group_list: 
                    sign_in_screen(clientsocket,addr,clientdatasocket,addr_data,groupname,username)
                elif groupname == "CLIENT_ERR":
                    print "CLIENT ERROR | RETURNING TO sign_in_screen"
                    controller(clientsocket,addr,clientdatasocket,addr_data)
            else:
                clientsocket.send("PASSWD-INCORRECT")
                controller(clientsocket, addr, clientdatasocket, addr_data)
    print "Exiting sign_in"

def sign_up_group(clientsocket,addr,clientdatasocket,addr_data,groupname,username,groupnames):
    print "GROUP SIGN UP -in sign_up_group"
    if groupname == "1":
        print "JOIN GROUP"
        join_group(clientsocket,addr,clientdatasocket,addr_data,groupnames,username)
        print "RETURN from join group"
    elif groupname == "2":
        print "LEAVE GROUP"
        leave_group(clientsocket,addr,clientdatasocket,addr_data,groupnames,username)
    else:
        print "INVALID OPTION"
def leave_group(clientsocket,addr,clientdatasocket,addr_data,groupnames,username):
    db = MySQLdb.connect("Jeet.local","root","heythere",database=broadcastdb )
    cursor = db.cursor()
    print "INSIDE LEAVE_GROUP WAITING TO RECEIVE choice"
    choice=(clientsocket.recv(1024))
    tempname=int(groupnames)
    print tempname,choice
    temp=tempname
    if choice == '1':
        if temp%10 == '1':
            tempname=tempname - 1;

    temp=temp/10
    if choice == '2':
        if temp%10 == 2:
            tempname=tempname - 2*10;
    temp=temp/10   
    if choice == '3':
        if temp%10 == 3: 
            tempname=tempname - 3*100;
    temp=temp/10
    if choice == '4':
        print choice,"temp | ",temp,"Tempname | ",tempname
        if temp %10 == 4:
            tempname=tempname - 4*1000;
    temp=temp/10
    if choice == '5':
        if temp%10 == 5:
            tempname=tempname - 5*10000;
    
    print "TEMPNAME | ",tempname
    print "GROUPNAME | ",groupnames
    groupnames=tempname
    print "GROUPNAME | ",groupnames
    
    sql="""UPDATE BROADCASTING_TABLE SET GROUPNAME=('%s') WHERE USERNAME=('%s')""" % (groupnames,username)
    # sql="""INSERT INTO BROADCASTING_TABLE (USERNAME,PASSWORD,IP,GROUPNAME) VALUES ('%s','%s','%s','%d')""" % (username,passwd,addr[0],groupname) 
    try:
        cursor.execute(sql)
        print "ADDED ENTRY TO THE DATABASE"
        db.commit()
        
    except:
        print "UNABLE TO ADD TO THE DATABASE"
        db.rollback()  
    sql="""SELECT * FROM BROADCASTING_TABLE"""
    cursor.execute(sql)
    result=cursor.fetchall()
    print "printing table contents"
    for res in result:
        print res
    db.close() 

def join_group(clientsocket,addr,clientdatasocket,addr_data,groupnames,username):
    db = MySQLdb.connect("Jeet.local","root","heythere",database=broadcastdb )
    cursor = db.cursor()
    print "INSIDE JOIN_GROUP WAITING TO RECEIVE choice"
    choice=(clientsocket.recv(1024))
    # groupname=0
    tempname=int(groupnames)
    print tempname
    temp=tempname
    if choice == '1':
        if temp%10 != 1:
            tempname=tempname + 1;
    temp=temp/10
    if choice == '2':
        if temp%10 != 2:
            tempname=tempname + 2*10;
    temp=temp/10   
    if choice == '3':
        if temp%10 != 3: 
            tempname=tempname + 3*100;
    temp=temp/10
    if choice == '4':
        if temp %10 != 4:
            tempname=tempname + 4*1000;
    temp=temp/10
    if choice == '5':
        if temp%10 != 5:
            tempname=tempname + 5*10000;
    print "TEMPNAME | ",tempname
    print "GROUPNAME | ",groupnames
    groupnames=tempname
    print "GROUPNAME | ",groupnames

    sql="""UPDATE BROADCASTING_TABLE SET GROUPNAME=('%s') WHERE USERNAME=('%s')""" % (groupnames,username)
    # sql="""INSERT INTO BROADCASTING_TABLE (USERNAME,PASSWORD,IP,GROUPNAME) VALUES ('%s','%s','%s','%d')""" % (username,passwd,addr[0],groupname) 
    try:
        cursor.execute(sql)
        print "ADDED ENTRY TO THE DATABASE"
        db.commit()
        
    except:
        print "UNABLE TO ADD TO THE DATABASE"
        db.rollback()  
    sql="""SELECT * FROM BROADCASTING_TABLE"""
    cursor.execute(sql)
    result=cursor.fetchall()
    print "printing table contents"
    for res in result:
        print res
    db.close()     


def sign_in_screen(clientsocket,addr,clientdatasocket,addr_data,groupname,username):
    print "Inside sign_in_screen"
    message=clientsocket.recv(1024)
    print "Received message | ",message
    # print "Received message is | ",message
    if message == "CHAT":
        print "CHATTING WINDOW | "
        clientsocket.send("dump")
        choice=clientsocket.recv(1024)
        
        if choice == "1":
            show_log(clientsocket,addr,clientdatasocket,addr_data,groupname,username,"Message_log.txt")
            sign_in_screen(clientsocket,addr,clientdatasocket,addr_data,groupname,username)

        elif choice == "2":
            receiver(clientsocket,addr,clientdatasocket,addr_data,groupname,username)
            sign_in_screen(clientsocket,addr,clientdatasocket,addr_data,groupname,username)
        else:
            print "INVALID CHOICE"
            sign_in_screen(clientsocket,addr,clientdatasocket,addr_data,groupname,username)

    elif message == "SIGN_OUT":
        
        if groupname == "IITGN":
            print "Inside IITGN"
            socket_list_group_1.remove(clientdatasocket)
                
        if groupname == "ENGINEERING":
            socket_list_group_2.remove(clientdatasocket)
        
        if groupname == "MATLAB":
            socket_list_group_3.remove(clientdatasocket)
            
        if groupname == "PYTHON":
            socket_list_group_4.remove(clientdatasocket)
            
        if groupname == "ENTREPRENEUR":
            socket_list_group_5.remove(clientdatasocket)
        
        # controller(clientsocket,addr,clientdatasocket,addr_data)
        
    elif message == "ls":
        print "Received ls command"
        list_file(clientsocket,groupname)
        sign_in_screen(clientsocket,addr,clientdatasocket,addr_data,groupname,username)
    elif message == "rm":
        remove_file(clientsocket,addr,clientdatasocket,addr_data,groupname,username)
        sign_in_screen(clientsocket,addr,clientdatasocket,addr_data,groupname,username)
    elif message == "SHARE":
        sharing_wizard(clientsocket,addr,clientdatasocket,addr_data,groupname,username)
        sign_in_screen(clientsocket,addr,clientdatasocket,addr_data,groupname,username)
    elif message == "DOWNLOAD":
        download_wizard(clientsocket,addr,clientdatasocket,addr_data,groupname,username)
        sign_in_screen(clientsocket,addr,clientdatasocket,addr_data,groupname,username)
    elif message == "UPLOAD":
        upload_wizard(clientsocket,addr,clientdatasocket,addr_data,groupname,username)
        # update_log(addr,groupname,"UPLOAD",username)
        sign_in_screen(clientsocket,addr,clientdatasocket,addr_data,groupname,username)
    elif message == "cat":
        show_log(clientsocket,addr,clientdatasocket,addr_data,groupname,username,"log.txt")
        sign_in_screen(clientsocket,addr,clientdatasocket,addr_data,groupname,username)
    else:
        print "To controller checkpoint" 
        # controller(clientsocket,addr,clientdatasocket,addr_data)
def update_log(filename,username,action,groupname,addr):
    print "UPDATE LOG MODULE"
    file=os.path.join(os.path.join(os.getcwd(),groupname),"log.txt")
    print "Filepath | ",file
    f=open(file,"a")
    write_line="\n"+str(filename)+"\t"+(username)+"\t"+(action)+"\t"+(groupname)+"\t"+str(addr[0])+"\t"+str(time.ctime())+"\n"
    f.writelines(write_line)
    f.close()

def show_log(clientsocket,addr,clientdatasocket,addr_data,groupname,username,flname):
    print "SHOW_LOG"
    filename=os.path.join(os.path.join(os.getcwd(),groupname),flname)
    print "Filename is | ",filename
    filesize=os.path.getsize(filename)
    print "Filesize | ",filesize
    clientsocket.send(str(filesize))
    print "Ready to send log file | ",filesize,filename
    
    # clientdatasocket.send(1024)
    if os.path.isfile(filename):
        with open(filename,'rb') as f:
            kBtoSend=f.read(1024)
            print "Read data | ",kBtoSend
            clientdatasocket.send(kBtoSend)
            print kBtoSend
            # dummy=clientdatasocket.recv(1024)
            while kBtoSend != "":
                kBtoSend=f.read(1024)
                # print "waiting for data"
                clientdatasocket.send(kBtoSend)
                print "sending data"
                time.sleep(0.5)
                # dummy=clientdatasocket.recv(1024)
                # print kBtoSend,dummy
            print "FILE SENT"
    else:
        print "FILE ERROR"

def upload_wizard(clientsocket,addr,clientdatasocket,addr_data,groupname,username):
    print "UPLOAD_WIZARD"
    filename=clientsocket.recv(1024)
    print filename
    if filename == "ERR":
        print "INVALID FILE NAME ENTERED BY CLIENT"
        # upload_wizard(clientsocket,addr,clientdatasocket,addr_data,groupname,username)
    else:
        print "Server ready to receive"
        clientsocket.send("READY_TO_RECEIVE")
        print "Sent READY TO RECEIVE"
        filesize=clientsocket.recv(1024) #
        group_dir=os.path.join(os.getcwd(),groupname)
        print "Group directory to write | ",group_dir
        f=open(os.path.join(group_dir,filename),'wb')
        print "File opened to write to"
        kBtoReceive=clientdatasocket.recv(1024)
        print "First kB receiveed | ",kBtoReceive
        totReceived=len(kBtoReceive)
        f.write(kBtoReceive)
        while str(totReceived) < filesize:
            print "Waiting to receive"
            kBtoReceive=clientdatasocket.recv(1024)
            
            print "KBs received | ",kBtoReceive
            totReceived+=len(kBtoReceive)
            f.write(kBtoReceive)
            print "Received | ",totReceived,"Filesize | ",filesize
            print type(totReceived),type(filesize)
            if totReceived == filesize:
                print "breaking"
                break

        print "FILE SUCCESSFULLY RECEIVED"
        update_log(filename,username,"UPLOAD",groupname,addr)
        f.close()

def download_wizard(clientsocket,addr,clientdatasocket,addr_data,groupname,username):

    flist=[]
    string="-"  

    for dirpath,dirname,filenames in os.walk(os.getcwd()):
        # print "Direcotry name | ", dirname," filename | ",filenames
        print "Directory path | ",dirpath,"What I made | ",os.path.join(os.getcwd(),groupname)
        if dirpath == os.path.join(os.getcwd(),groupname):
            print filenames
            for fn in filenames:
                flist.append(fn)
                print "Appended ",fn, " to ",flist
            string=string.join(flist)
    print "Return from ls | ",string
    clientsocket.send(string)


    filename = clientsocket.recv(1024)
    path_to_find = os.path.join(os.getcwd(),groupname)
    if os.path.isfile(os.path.join(path_to_find,filename)):
        clientsocket.send("EXIST "+ str(os.path.getsize(os.path.join(path_to_find,filename))))
        message=clientsocket.recv(1024)
        if message == "OK":
            print "OPENING FILE TO READ AND SEND THE FILE FROM |",str(os.path.join(path_to_find,filename))
            with open(os.path.join(path_to_find,filename),'rb') as f:
                kBtoSend=f.read(1024)
                print "Sending | ",kBtoSend
                clientdatasocket.send(kBtoSend)
                while kBtoSend != "":
                    kBtoSend=f.read(1024)
                    print "Sending | ",kBtoSend
                    clientdatasocket.send(kBtoSend)
                print "FILE SENT"
                update_log(filename,username,"DOWNLOAD",groupname,addr)
    else:
        print "FILE DOES NOT EXIST"
        clientsocket.send("DOES_NOT_EXIST")

def sharing_wizard(clientsocket,addr,clientdatasocket,addr_data,groupname,username):
    "This creates a symlink of the src file in the dst file. format: os.symink(src,dst)"
    clientsocket.send("READY_TO_SHARE")
    filename=clientsocket.recv(1024)
    print "File  to share | ",filename
    path_to_file=(os.path.join(os.getcwd(),groupname))
    isfile=os.path.isfile(os.path.join(path_to_file,filename))
    if isfile:
        print "FILE EXIST"
        clientsocket.send("OK")
        message=clientsocket.recv(1024)
        update_log(filename,username,"SHARE",groupname,addr)
        if message == "1":
            try:
                os.symlink(os.path.join(path_to_file,filename),os.path.join(os.path.join(os.getcwd(),group_list[0]),filename))
                print "SYMBOLIC LINK CREATED"
                clientsocket.send("SYMLINK_CREATED")
            except:
                print "SYMBOLIC LINK CANNOT BE CREATED"
        elif message == "2":
            print "Sharing file with group",group_list[1]
            try:
                print "Source | ",os.path.join(path_to_file,filename), "Destination | ",os.path.join(os.getcwd(),group_list[1])
                os.symlink(os.path.join(path_to_file,filename),os.path.join(os.path.join(os.getcwd(),group_list[1]),filename))
                print "SYMBOLIC LINK CREATED"
                clientsocket.send("SYMLINK_CREATED")
            except:
                print "SYMBOLIC LINK CANNOT BE CREATED"
        elif message == "3":
            try:
                os.symlink(os.path.join(path_to_file,filename),os.path.join(os.path.join(os.getcwd(),group_list[2]),filename))
                print "SYMBOLIC LINK CREATED"
                clientsocket.send("SYMLINK_CREATED")
            except:
                print "SYMBOLIC LINK CANNOT BE CREATED"
        elif message == "4":
            try:
                os.symlink(os.path.join(path_to_file,filename),os.path.join(os.path.join(os.getcwd(),group_list[3]),filename))
                print "SYMBOLIC LINK CREATED"
                clientsocket.send("SYMLINK_CREATED")
            except:
                print "SYMBOLIC LINK CANNOT BE CREATED"
        elif message == "5":
            try:
                os.symlink(os.path.join(path_to_file,filename),os.path.join(os.path.join(os.getcwd(),group_list[4]),filename))
                print "SYMBOLIC LINK CREATED"
                clientsocket.send("SYMLINK_CREATED")
            except:
                print "SYMBOLIC LINK CANNOT BE CREATED"
        else:
            print "INVALID RESPONSE PLEASE CHECK"
    else:
        print "File does not exist"
        clientsocket.send("FILE_DOES_NOT_EXIST")


def remove_file(clientsocket,addr,clientdatasocket,addr_data,groupname,username):
    list_file(clientsocket,groupname)
    filename=clientsocket.recv(1024)
    path_to_file=(os.path.join(os.getcwd(),groupname))
    try:
        os.remove(os.path.join(path_to_file,filename))
        print "File | ",filename," removed successfully"
        clientsocket.send("RM_SUCCESS")
        update_log(filename,username,"DELETE",groupname,addr)
    except:
        print "Unable to remove file | ",filename
        clientsocket.send("RM_FAILED")

def list_file(clientsocket,groupname):
    print "Trying to list files inside directory ",groupname
    # directory=groupname
    flist=[]
    string="-"  

    for dirpath,dirname,filenames in os.walk(os.getcwd()):
        # print "Direcotry name | ", dirname," filename | ",filenames
        print "Directory path | ",dirpath,"What I made | ",os.path.join(os.getcwd(),groupname)
        if dirpath == os.path.join(os.getcwd(),groupname):
            print filenames
            for fn in filenames:
                flist.append(fn)
                print "Appended ",fn, " to ",flist
            string=string.join(flist)
    print "Return from ls | ",string
    clientsocket.send(string)
def message_logger(clientsocket,addr,clientdatasocket,addr_data,groupname,username,message):
    print "MESSAGE LOGGER"
    filename=os.path.join(os.getcwd(),os.path.join(groupname,"Message_log.txt"))
    print filename
    f=open(filename,'a')
    write_lines=username+"\t"+time.ctime()+"\t"+message
    f.writelines(write_lines)

def receiver(clientsocket,addr,clientdatasocket,addr_data,groupname,username):
    # print "In receiver"
    db = MySQLdb.connect("Jeet.local","root","heythere",database=broadcastdb )
    cursor = db.cursor()
    print "Starting the receiver"
    while 1:
        # print clientdatasocket, "Are you receiving from it ?"
        message = clientdatasocket.recv(1024)
        print "Received | ",message
        if message != ":q":
            message_logger(clientsocket,addr,clientdatasocket,addr_data,groupname,username,message)
        if not message:
            print ("No dta received")
            break
        elif message == ":q":
            print "Received quit, sending it to shut client receiver down"
            clientdatasocket.send(":q")
            sign_in_screen(clientsocket,addr,clientdatasocket,addr_data,groupname,username)
        else:
            print addr, ' >> ', message, "groupname | ",groupname
            # message=s_data.recv(1024)
            if groupname == "IITGN":
                print "Insdie IITGN"
                for cs in socket_list_group_1:
                    if cs != clientdatasocket:
                        cs.send(message)
                        print "Clientdatasocket | ",cs," message | ",message
                        
            if groupname == "ENGINEERING":
                print "INSIDE engineering"
                for cs in socket_list_group_2:
                    if cs != clientdatasocket:
                        cs.send(message)
                        print "Clientdatasocket | ",cs," message | ",message
                        
            if groupname == "MATLAB":
                print "Inside MATLAB"
                for cs in socket_list_group_3:
                    if cs != clientdatasocket:
                        print "Clientdatasocket | ",cs," message | ",message
                        cs.send(message)
            if groupname == "PYTHON":
                for cs in socket_list_group_4:
                    if cs != clientdatasocket:
                        print "Clientdatasocket | ",cs," message | ",message
                        cs.send(message)
            if groupname == "ENTREPRENEUR":
                for cs in socket_list_group_5:
                    if cs != clientdatasocket:
                        print "Clientdatasocket | ",cs," message | ",message
                        cs.send(message)
                        
	print "Closing socket"    

    # clientdatasocket.close()
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
    # message=
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
    # delete_database()
    create_broadcast_database()
    # delete_table()
    create_broadcast_table()
    create_dir() #OS function

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

def create_dir():
    "This function will create the directory once a user creates a public group"
    "This function will call the update the log file reporting the creation of the group+the username of its creator"
    for gl in group_list:
        try:
            os.mkdir(gl)
        except:
            print "Directory ",gl," exist"
    cwd=os.getcwd()
    for gl in group_list:
        try:    
            print os.path.join(cwd,gl)
            os.chdir(os.path.join(cwd,gl))
            print os.getcwd()
            print os.path.join(os.path.join(cwd,gl),"log.txt")
            if os.path.isfile(os.path.join(os.path.join(cwd,gl),"log.txt")):
                print "FILE EXIST", os.path.isfile(os.path.join(os.path.join(cwd,gl)),"log.txt")
            else:
                f=open("log.txt",'w')
                print "creating log.txt"
                write_line=("FILENAME")+"\t"+("USERNAME")+"\t"+("ACTION")+"\t"+("GROUPNAME")+"\t"+("IP")+"\t"+("DATE  TIME")+"\n\n"
                f.writelines(write_line)
                f.close()
            # for dirpath,dirlist,filelist in os.walk(cwd):
            #     print filelist
            if os.path.isfile(os.path.join(os.path.join(cwd,gl),"Message_log.txt")):
                print "FILE EXIST"
            else:
                f=open("Message_log.txt",'w')
                print "creating message Message_log.txt"
                write_line="USERNAME"+"\t"+"TIMESTAMP"+"\t"+"MESSAGE"+"\n\n"
                f.writelines(write_line)
                f.close()
        except:
            print "LOG FILE ALREADY EXIST"
        print cwd
        os.chdir(cwd)
    # return 0

if __name__ == '__main__':
	Main()
