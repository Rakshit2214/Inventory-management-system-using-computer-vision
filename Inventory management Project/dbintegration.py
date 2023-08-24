import mysql.connector
def updatevals(pname,clist):
    conn = mysql.connector.connect(user = 'root',
                                host = 'localhost',
                               password = 'root',
                              database = 'invmanager')
    cursor = conn.cursor()

    query1 = """SELECT count from inv where name =%s"""
    query2="""UPDATE inv SET count = %s Where name= %s"""
    for i in range(len(pname)):
        data =[(pname[i])]
        cursor.execute(query1,data)
        cnttemp = cursor.fetchall()
        
        d2 = [(cnttemp[0][0]+clist[i]),(pname[i])]
        cursor.execute(query2,d2)
        conn.commit()
    conn.close()


def updatevals2(pname,clist):
    
    conn = mysql.connector.connect(user = 'root',
                                host = 'localhost',
                               password = 'root',
                              database = 'invmanager')
    cursor = conn.cursor()

    query1 = """SELECT count from inv where name =%s"""
    query2="""UPDATE inv SET count = %s Where name= %s"""
    for i in range(len(pname)):
        data =[(pname[i])]
        cursor.execute(query1,data)
        cnttemp = cursor.fetchall()
        
        d2 = [(cnttemp[0][0]-clist[i]),(pname[i])]
        cursor.execute(query2,d2)
        conn.commit()
    conn.close()

def retname():
    conn = mysql.connector.connect(user = 'root',
                                host = 'localhost',
                               password = 'root',
                              database = 'invmanager')
    cursor = conn.cursor()

    query = """SELECT name from inv """
    cursor.execute(query)
    dispname = cursor.fetchall()
    return dispname 
    conn.close()

def retcount():
    conn = mysql.connector.connect(user = 'root',
                                host = 'localhost',
                               password = 'root',
                              database = 'invmanager')
    cursor = conn.cursor()

    query = """SELECT count from inv """
    cursor.execute(query)
    dispcount = cursor.fetchall()
    return dispcount 
    conn.close()