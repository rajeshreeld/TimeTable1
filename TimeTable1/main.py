import dataAccessSQLAlchemy as da
import pandas as pd
import random
import numpy as np
print("welcome");

# Combine subjectBatchTeacher and subjectClassTeacher

f_join_subject_subjectClassTeacher = da.execquery('select s.subjectId, subjectShortName, totalHrs, eachSlot, c.classId, teacherId from subject s, subjectClassTeacher c where s.subjectId = c.subjectId;')
f_join_subject_subjectClassTeacher.insert(5,'batchId','-')
f_join_subject_subjectClassTeacher.insert(6,'category','T') #T for theory
f_join_subject_subjectBatchTeacher = da.execquery('select s.subjectId, subjectShortName, totalHrs, eachSlot, sbt.batchId, bc.classId from subject s, subjectBatchTeacher sbt, batchClass bc where s.subjectId = sbt.subjectId AND sbt.batchId = bc.batchId;')
f_join_subject_subjectBatchTeacher.insert(6,'category','L') #L for Lab

f_subjectBatchClassTeacher = pd.concat([f_join_subject_subjectClassTeacher, f_join_subject_subjectBatchTeacher])
#print (f_subjectBatchClassTeacher)

x = f_subjectBatchClassTeacher;
x.reset_index();

totallectures_list = (x['totalHrs'] / x['eachSlot'])


# Create empty dataframe to save all the requirements
req_all = pd.DataFrame(index=range(int(totallectures_list.sum())), columns=list(x))
j = 0

# Save all requirements in the data frame
for i in range(len(req_all)):
    if((x.iloc[j]['totalHrs']/x.iloc[j]['eachSlot'])>0):
        req_all.loc[[i]] = x.iloc[[j]].values
        x.set_value(j,'totalHrs', x.loc[j]['totalHrs'] - x.loc[j]['eachSlot'])
    if (x.iloc[j]['totalHrs'] == 0):
        j = j + 1
#print(req_all)


#These values need to be calculated from the database
n_classes = 14
n_days = 5
n_slots = 10
n_maxlecsperslot = 4
timetable_np = np.empty((n_classes, n_days, n_slots, n_maxlecsperslot))*np.nan

for c in (set(req_all.classId)):         #First take one class
    #print(c)
    #http://stackoverflow.com/questions/17071871/select-rows-from-a-dataframe-based-on-values-in-a-column-in-pandas
    req_forgivenclass=req_all.loc[req_all['classId'] == c]      #List all the requirements for that class in req_forgivenclass
    #print(req_forgivenclass)
    #print(set(req_forgivenclass.index))        #These are the indices of the requirements for this class
    for req in set(req_forgivenclass.index):    #Schedule each of these requirements
        notassigned = 1
        while(notassigned==1):      #Keep on scheduling till not found
            r_day=random.randint(0,n_days-1)
            r_slot = random.randint(0, n_slots-1)
            r_lecnumber=random.randint(0,n_maxlecsperslot-1)
            if(np.isnan(np.sum(timetable_np[c,r_day,r_slot,r_lecnumber]))):   #Check if that slot is empty, this way of using np.isnan is the fastest way of doing so
                timetable_np[c,r_day,r_slot,r_lecnumber] = req
                #print("Asigned")
                notassigned=0
            #else:
                #print("Not found")
    #print(timetable_np[c,:,:,:])


#For all classes, day d and slot s
d = 2;
s = 3;
one_day_slot = timetable_np[:, d, s, :];

for row in one_day_slot:
    for col in row:
        if not np.isnan(col):
            print (req_all.loc[req_all.index == col])


    
