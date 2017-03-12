import sqlalchemy as sql
import pymysql as py
import pandas as pd
import  entities as ent

# Class for conencting to database
class DB:

    def getConnection (self):
        engine = sql.create_engine('mysql+pymysql://root:Admin@123@localhost/timetable');

        #print(engine.table_names());
        con = engine.connect();
        return con;

    def close (self,con):
        con.close();

# Initialization method to initialize all frames
def initialize (table_name):
    db = DB();
    
    con = db.getConnection();
    frame = pd.read_sql_table(table_name, con);

    db.close(con);

    return frame;


print("welcome");

# Required frames
f_subject = initialize('subject');
f_class = initialize('class');
f_teacher = initialize('teacher');
f_room = initialize('room');
f_batch = initialize('batch');
f_batchClass = initialize('batchclass'); #Name of table is batchClass,python is taking batchglass
f_subjectClassTeacher = initialize('subjectclassteacher');

print(f_subjectClassTeacher);