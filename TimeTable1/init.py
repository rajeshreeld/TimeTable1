import pandas as pd

print("Welcome to the timetable problem!!! :D :D :D ")

#Loading data structures
subject=pd.read_csv("subject.csv")
batch=pd.read_csv("batch.csv")
class_d=pd.read_csv("class.csv")
batch=pd.read_csv("batch.csv")
teacher=pd.read_csv("teacher.csv")
subject_teacher=pd.read_csv("subject-teacher.csv")
subject_batch=pd.read_csv("subject-batch.csv")
class_subject=pd.read_csv("class-subject.csv")
timetable=pd.read_csv("timetable.csv")

#Printing heads of tables
print("printing the headers of the tables")
print(subject.head(0))
print(batch.head(0))
print(class_d.head(0))
print(batch.head(0))
print(teacher.head(0))
print(subject_batch.head(0))
print(class_subject.head(0))
print(subject_teacher.head(0))
print(timetable.head(0))
#day, slotNo, roomId, classId, subjectId , teacherId, batchId, isBreak
#print(timetable)

x=subject.join(subject_batch.set_index('subjectID'), on='subjectID')
print(x.head(10))
y=x.join(batch.set_index('batchID'), on='batchID')
y=y.reset_index(drop=True)
print(y.head(10))
totallectures_list=(y['totalHrs']/y['eachSlot'])

##Create empty dataframe to save
#new_y = pd.DataFrame(index=range(int(totallectures_list.sum())), columns=list(y))
#j=0
#for i in range(len(new_y)):
#    print(i)
#    #if((y[j]['totalHrs']/y[j]['eachSlot'])>0):
#    new_y.iloc[[i]]=y.iloc[[j]]
#    y.loc[j]['totalHrs']=y.loc[j]['totalHrs']-y.loc[j]['eachSlot']
#    if(y.iloc[j]['totalHrs']==0):
#        j=j+1
#print(new_y)    
    