import dataAccessSQLAlchemy as da
import pandas as pd
import numpy
import random
import numpy as np
print("welcome");

def teacher_overlap(timetable):
    teacher_cost = 0
    for day in range(n_days):
        for slot in range (n_slots):
            temp_array = timetable[:, day, slot, :]
            teacher_list = []
            print(temp_array)
            for row in temp_array:
                for cell in row:
                    if not np.isnan(cell):
                        req = req_all.loc[req_all.index == cell]
                        teacher_list.append(req.iloc[0]['teacherId'])
            for teacher_id in teacher_list:
                if teacher_id is not None:
                    teacher_cost = teacher_cost + teacher_list.count(teacher_id) - 1

    return teacher_cost

f_join_subject_subjectClassTeacher = da.execquery('select s.subjectId, subjectShortName, totalHrs, eachSlot, c.classId from subject s, subjectClassTeacher c where s.subjectId = c.subjectId;')
f_join_subject_subjectClassTeacher.insert(5,'batchId','-')
f_join_subject_subjectClassTeacher.insert(6,'category','T') #T for theory
#f_join_subject_subjectClassTeacher.rename(columns={'classId':'classOrBatchId'}, inplace=True)
#print(f_join_subject_subjectClassTeacher)
f_join_subject_subjectBatchTeacher = da.execquery('select s.subjectId, subjectShortName, totalHrs, eachSlot, sbt.batchId, bc.classId from subject s, subjectBatchTeacher sbt, batchClass bc where s.subjectId = sbt.subjectId AND sbt.batchId = bc.batchId;')
f_join_subject_subjectBatchTeacher.insert(6,'category','L') #L for Lab
#f_join_subject_subjectBatchTeacher.rename(columns={'batchId':'classOrBatchId'}, inplace=True)
#print(f_join_subject_subjectBatchTeacher)

f_subjectBatchClassTeacher = pd.concat([f_join_subject_subjectClassTeacher, f_join_subject_subjectBatchTeacher])
print (f_subjectBatchClassTeacher)
#f_subjectBatchClassTeacher.to_csv("s-b-c-t.csv")


#x = f_subject.join(f_subjectBatchTeacher.set_index('subjectId'), on='subjectId')
x=f_subjectBatchClassTeacher
x=x.reset_index()
print(x.head(20))
print(x.tail())
x.to_csv("x.csv")
totallectures_list = (x['totalHrs'] / x['eachSlot'])
print(totallectures_list)


# Create empty dataframe to save all the requirements
req_all = pd.DataFrame(index=range(int(totallectures_list.sum())), columns=list(x))
j = 0
for i in range(len(req_all)):
    if((x.iloc[j]['totalHrs']/x.iloc[j]['eachSlot'])>0):
        req_all.loc[[i]] = x.iloc[[j]].values
        x.set_value(j,'totalHrs', x.loc[j]['totalHrs'] - x.loc[j]['eachSlot'])
    if (x.iloc[j]['totalHrs'] == 0):
        j = j + 1
print(req_all)

req_all.to_csv("req_all.csv")

# Create new panel
#timetable1 = pd.panel4D(items=10, major_axis=5, minor_axis=10, dtype=int)  # Check if we can do something by dtype = some class here
#print(timetable1)
#timetable1[3][2][4] = 7
#print(timetable1[3])
#These values need to be calculated from the database
n_classes=14
n_days=5
n_slots=10
n_maxlecsperslot=5
timetable_np = np.empty((n_classes, n_days, n_slots, n_maxlecsperslot))*np.nan
print(timetable_np)
for c in (set(req_all.classId)):    #First take one class
    print(c)
    #http://stackoverflow.com/questions/17071871/select-rows-from-a-dataframe-based-on-values-in-a-column-in-pandas
    req_forgivenclass=req_all.loc[req_all['classId'] == c]      #List all the requirements for that class in req_forgivenclass
    print(req_forgivenclass)
    #print(set(req_forgivenclass.index))     #These are the indices of the requirements for this class
    for req in set(req_forgivenclass.index):    #Schedule each of these requirements
        notassigned = 1
        while(notassigned==1):      #Keep on scheduling till not found
            r_day=random.randint(0,n_days-1)
            r_slot = random.randint(0, n_slots-1)
            r_lecnumber=random.randint(0,n_maxlecsperslot-1)
            if(np.isnan(np.sum(timetable_np[c,r_day,r_slot,r_lecnumber]))):   #Check if that slot is empty, this way of using np.isnan is the fastest way of doing so
                timetable_np[c,r_day,r_slot,r_lecnumber]=req
                #print("Asigned")
                notassigned=0
            #else:
                #print("Not found")
    print(timetable_np[c,:,:,:])

teacher_cost = teacher_overlap(timetable_np)
print("Teacher cost:")
print(teacher_cost)