import sqlalchemy as sql
import pymysql as py
import pandas as pd
import  entities as ent


class DB:

    def getConnection (self):
        engine = sql.create_engine('mysql+pymysql://root:Admin@123@localhost/timetable');
        con = engine.connect();
        return con;

    def close (self,con):
        con.close();

def initialize (table_name):
    db = DB();
    
    con = db.getConnection();
    frame = pd.read_sql_table(table_name, con);

    db.close(con);

    return frame;


print("welcome");
frame = initialize('teacher');

print(frame);