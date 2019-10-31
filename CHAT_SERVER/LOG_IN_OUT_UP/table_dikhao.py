import MySQLdb

database_name='CHAT_SERVER_DATABASE'

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
    name="JEET THE GREAT"
    try:
        print "Trying to insert values to the tables"
        sql="INSERT INTO CHAT_SERVER (USERNAME,IP) VALUES ('%s','%d')" % ('Jitesh',20)
        print "truncating table"
        sql="""DROP TABLE CHAT_SERVER"""
        cursor.execute(sql)
    except:
        print "Unable to add values to the table"
    # cursor.execute("SELECT * FROM CHAT_SERVER")
    # results=cursor.fetchone()
    # # for pt in results:
    # print "Values in the table",results
        # print row[0],row[1]
    sql="""SHOW TABLES"""
    cursor.execute(sql)
    for df in cursor:
        print df
    db.close()

if __name__ == '__main__':
    create_database()
