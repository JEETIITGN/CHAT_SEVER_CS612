import MySQLdb

database_name='CHAT_SERVER_DATABASE'
def play_database():
    print "Inside play with database"
    db = MySQLdb.connect("Jeet.local","root","heythere",database=database_name )
    print "Making the cursor to database"
    cursor = db.cursor()
    

    # cursor.execute(sql)
    try:
        print "Defining variable sql to write to the database"
        sql = """CREATE TABLE CHAT_SERVER (
         USERNAME  CHAR(20) NOT NULL,
         IP INT )"""
        print "Executing the table creation command to the database"
        cursor.execute(sql)
        db.commit() #db is the file descriptor for our database commit would write the changes
    except:
        print "Table already created"
        db.rollback()#rollback would undo the cursor.execute(sql) command

    cursor.execute("SHOW TABLES")
    for tb in cursor:
        print tb
    sql=""" """
    # cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
    # Fetch a single row using fetchone() method.
    # data = cursor.fetchone()
    # print "Database version : %s " % data
    # disconnect from server
    db.close()

def create_database():
    
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

    db.close()
def delete_database():
    db = MySQLdb.connect("Jeet.local","root","heythere",database=database_name )
    print ("Database creation successful with database descriptor: ", db)
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    sql="SHOW TABLES"
    cursor.execute(sql)

    for cu in cursor:
        print "Dropping",cu
        sql="DROP TABLE '%s'" % (cu)
    for cu in cursor:
        print cu    
    print "Done deleting database"
    db.close()
if __name__ == '__main__':
    create_database()
    play_database()
    delete_database()
