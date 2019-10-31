import MySQLdb

database_name='CHAT_SERVER_DATABASE'

def sign_UP():
    print "Inside play with database"
    create_database()
    db = MySQLdb.connect("Jeet.local","root","heythere","CHAT_SERVER_DATABASE" )
    print "Making the cursor to database"
    cursor = db.cursor()
    username=raw_input("USERNAME | ")
    password=raw_input("PASSWORD | ")

    # cursor.execute(sql)
    try:
        print "Defining variable sql to write to the database",username,password
        sql="""SELECT USERNAME FROM CHAT_SERVER WHERE USERNAME IN ("%s")""" % (username)
        cursor.execute(sql)
        result=cursor.fetchall()
        if len(result) == 0:
            sql="INSERT INTO CHAT_SERVER (USERNAME,PASSWORD) VALUES ('%s','%s')" % (username,password)
            cursor.execute(sql)
            print "Executing the table creation command to the database"
            db.commit() #db is the file descriptor for our database commit would write the changes
        else:
            print "USERNAME ",username," already in use! Returning to main window now." 
    except:
        print "Unable to add row to the table"
        db.rollback()#rollback would undo the cursor.execute(sql) command

    sql=("SELECT * FROM CHAT_SERVER")
    try:
        cursor.execute(sql)
        result=cursor.fetchall()

        # results =cursor.fetchall()
        for df in result:

            print "Trying to show the content of the table",df
    except:
        print "Unable to display the content of the table"
    # cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
    # Fetch a single row using fetchone() method.
    # data = cursor.fetchone()
    # print "Database version : %s " % data
    # disconnect from server
    # db.close()
def sign_in():
    print "MENU FOR SIGNING IN"
    username=raw_input("USERNAME | ")
    password=raw_input("PASSWORD | ")
    create_database()
    db = MySQLdb.connect("Jeet.local","root","heythere",database=database_name )
    print ("Database creation successful with database descriptor: ", db)
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    try:
        print "Inside try block in sign_in"
        sql="""SELECT * FROM CHAT_SERVER WHERE USERNAME IN ("%s")""" % (username)
        cursor.execute(sql)
        print "checking if username exists"
        result=cursor.fetchall()
        for values in result:
            usr=values[0]
            pas=values[1]
            print usr," ",pas
        if len(result) == 0:
            print "USERNAME ",username," does not exist returning to main window"
            main()
        else:
            print "USERNAME EXISTS"
            if password == pas:
                print "PASSWORD IS A MATCH SIGNING IN | "
                sign_in_pass()
    except:
        print "SORRY THE USERNAME DOES NOT EXIST RETURNING TO MAIN MENU"
        Main()

def create_database():
    print "Inside create database"
    db = MySQLdb.connect("Jeet.local","root","heythere",database=database_name )
    print ("Database creation successful with database descriptor: ", db)
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    print "Done creating database cursor"
    try:
        cursor.execute("CREATE DATABASE CHAT_SERVER_DATABASE")
        print "Database created successfully"
        db.commit()
    except:
        print "Database already exist"
        db.rollback()

    print "Displaying database cursor"
    cursor.execute("SHOW DATABASES")
    for dbs in cursor:
        print dbs
    try:
        print "Defining variable sql to write to the database"
        sql = """CREATE TABLE CHAT_SERVER (
         USERNAME  CHAR(20) NOT NULL,
         PASSWORD CHAR(20) NOT NULL )"""#The created table have the second entry that is receiving the integer value but I am trying to throw in string value
        print "Executing the table creation command to the database"
        cursor.execute(sql)
        db.commit() #db is the file descriptor for our database commit would write the changes
    except:
        print "Table already created"
        db.rollback()#rollback would undo the cursor.execute(sql) command
    
    print "EXITING CREATE_DATABASE"
    db.close()
def delete_database():
    db = MySQLdb.connect("Jeet.local","root","heythere",database=database_name )
    print ("Database creation successful with database descriptor: ", db)
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    sql="SHOW TABLES"
    cursor.execute(sql)

    try:
        print "Trying to insert values to the tables"
        print "Deleting table"
        sql="""DROP DATABASE ('%s')""" % (database_name)
        cursor.execute(sql)
    except:
        print "Unable to drop database"
    db.close()
def delete_table():
    db = MySQLdb.connect("Jeet.local","root","heythere",database=database_name )
    print ("Database creation successful with database descriptor: ", db)
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    print "Done creating database cursor"
    try:
        print "Deleting table"
        sql="""DROP TABLE CHAT_SERVER"""
        cursor.execute(sql)
    except:
        print "Unable to delete the table"
    db.close()
def admin():
    print "Enter the ADMIN password | "
    password=raw_input("PAssword | ")
    if password=="heythere":

        print "WELCOME JEET TO THE UNDERWORLD"
        print "Press 1: DELETE TABLES"
        print "Press 2: DELETE DATABASE"
        print "Any other key to return to main menu"
        choice = raw_input("Enter your choice | ")

        if choice == '1':
            delete_table()
        elif choice == '2':
            delete_database()
        else :
            Main()
    else:
        print "Incorrect password, returning to the main menu"
        Main()

def Main():
    
    print "Welcome to the club of elites."
    while 1:
        print "Press 1: Sign_IN"
        print "Press 2: Sign_UP"
        print "Press 3: EXIT"
        choice= raw_input("Enter you choice | ")

        if choice == '1':
            sign_in()
        elif choice == '2':
            sign_UP()
        elif choice == '5':
            admin()
        else:
            exit()

def sign_in_pass():
    print "SIGN IN SUCCESSFULLY"
    print "Press 1: List files"
    print "Press 2: Upload files"
    print "Press 3: Download files"
    print "Press 4: Delete files"
    print "Press 5: Share files"
    print "Press 6: Show log"
    print "Press 7: Sign out"
    choice= raw_input("Enter your choice | ")

    if choice == '1':
        list_files()
    elif choice == '2':
        upload_files()
    elif choice == '3':
        download_files()
    elif choice == '4':
        delete_files()
    elif choice == '5':
        share_files()
    elif choice == '6':
        show_log()
    else: 
        Main()
        
if __name__ == '__main__':
    Main()