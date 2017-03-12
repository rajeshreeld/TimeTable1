#import mysql.connector
#import TimeTable1;

#con = mysql.connector.connect(host="localhost", user = "root", password="Admin@123", database="timetable");

#query = ("SELECT * FROM class");

#cur = con.cursor();

#cur.execute(query);

#List = []
#for e in cur:
#    obj = TimeTable1.Class();

class myClass:

    def __init__(self, **kwargs):
        myClass.Name = kwargs[0]
        myClass.ID = kwargs[1];

    def display(self):
        print(self.Name, self.ID);

arg = {"Aditi", 23}
obj = myClass(arg);
obj.display();
#class Teacher:
#    TeacherID = 0
#    TeacherName = ""

#    def __init__(self, ID, Name):
#       self.TeacherID = ID
#       self.TeacherName = Name

#    def printData (self):
#        print (self.TeacherID, self.TeacherName);


#t = Teacher(1, "Aditi")
#t.printData();




