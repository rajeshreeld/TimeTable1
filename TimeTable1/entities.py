import csv

class Subject:
  
    def __init__(self, subjectID, subjectName, subjectsName, totalHrs, eachSlot, courseCode):
        self.SubjectID = subjectID
        self.SubjectName = subjectName
        self.SubjectShortName = subjectsName
        self.TotalHrs = totalHrs
        self.EachSlot = eachSlot
        self.CourseCode = courseCode

    def getData (self):
        print (self.SubjectID, self.SubjectName, self.SubjectShortName, self.TotalHrs,self.TotalHrs,self.CourseCode);
        

class Teacher:

    def __init__(self, teacherID, teacherName, teachersName, deptId, minHrs, maxHrs):
        self.TeacherID = teacherID
        self.TeacherName = teacherName
        self.TeacherShortName = teachersName
        self.DeptID = deptId
        self.MinHrs = minHrs
        self.MaxHrs = maxHrs

    def getData (self):
        print (self.TeacherID, self.TeacherName, self.TeacherShortName, self.DeptID,self.MinHrs,self.MaxHrs);

class Class:

    def __init__(self, classID, className, classsName):
        self.ClassID = classID
        self.ClassName = className
        self.ClassShortName = classsName
    
        def getData (self):
            print (self.ClassID, self.ClassName, self.ClassShortName);


class Batch:
    counter = 0

    def __init__(self, batchId, batchName, batchCount):
        self.BatchID = batchId
        self.BatchName = batchName
        self.BatchCount = batchCount
    def getData (self):
        print (self.BatchID, self.BatchName, self.BatchCount);

class BatchClass:

    def __init__(self, batchId, classId, batchName, batchCount):

        self.BatchID = Class.counter
        self.ClassID = classId
        self.BatchName = batchName
        self.BatchCount = batchCount

class Room:

    def __init__(self, roomId, roomName, roomsName, roomCount):
        self.RoomID = roomId
        self.RoomName = roomName
        self.RoomShortName = roomsName
        self.RoomCount = roomCount

    def getData (self):
        print (self.RoomID, self.RoomName, self.RoomShortName, self.RoomCount);


class BatchCanOverlap:

    def __init__(self, boId, batchId1, batchId2):
        self.BatchOverlapID = boId
        self.Batch1 = batchId1
        self.Batch2 = batchId2

    def getData (self):
        print (self.BatchOverlapID, self.Batch1, self.Batch2);


#class SubjectBatchTeacher:
#    counter = 0

#    def __init__(self, subjectID, batchId, teacherId):
#        self.SBTId = counter


#with open ('files/batch-can-overlap.csv', newline = '\n') as sub:
#    reader = csv.reader(sub);
#    List = []
#    for row in reader:
#        a = BatchCanOverlap(row[0], row[1]);
#        List.append(a);


#    for s in List:
#        s.getData();