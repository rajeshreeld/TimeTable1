import mysql.connector
import entities

host = "localhost"
user = "root"
password = "Admin@123"
database = "timetable"

class DB:

    def connectDB (self):
        con = mysql.connector.connect(host = host, 
                                  user = user,
                                  password = password,
                                  database = database); 

        return con;

    def close (con):
        con.close();



def initialize ():
    db = DB();

    query = ("SELECT * FROM subject");
    list = [];
    
    con = db.connectDB();
    cur = con.cursor();
    cur.execute(query);

    for r in cur.fetchall():
        sub = entities.Subject(r[0], r[1], r[2], r[3], r[4], r[5]);
        list.append(sub);

    for s in list:
        s.getData();

    con.close();

initialize();