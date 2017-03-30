import dataAccessSQLAlchemy as da
import pandas as pd

print("welcome");

f_join_subject_subjectClassTeacher = da.execquery('select s.subjectId, subjectShortName, totalHrs, eachSlot, c.classId from subject s, subjectClassTeacher c where s.subjectId = c.subjectId;')
f_join_subject_subjectClassTeacher.insert(5,'batchId','-')
f_join_subject_subjectClassTeacher.insert(6,'category','C')
#f_join_subject_subjectClassTeacher.rename(columns={'classId':'classOrBatchId'}, inplace=True)
#print(f_join_subject_subjectClassTeacher)
f_join_subject_subjectBatchTeacher = da.execquery('select s.subjectId, subjectShortName, totalHrs, eachSlot, sbt.batchId, bc.classId from subject s, subjectBatchTeacher sbt, batchClass bc where s.subjectId = sbt.subjectId AND sbt.batchId = bc.batchId;')
f_join_subject_subjectBatchTeacher.insert(6,'category','B')
#f_join_subject_subjectBatchTeacher.rename(columns={'batchId':'classOrBatchId'}, inplace=True)
#print(f_join_subject_subjectBatchTeacher)

f_subjectBatchClassTeacher = pd.concat([f_join_subject_subjectClassTeacher, f_join_subject_subjectBatchTeacher])
print (f_subjectBatchClassTeacher)
#f_subjectBatchClassTeacher.to_csv("s-b-c-t.csv")


#x = f_subject.join(f_subjectBatchTeacher.set_index('subjectId'), on='subjectId')
#x=x.reset_index()
#print(x.head(20))
#print(x.tail())
#x.to_csv("x.csv")
#totallectures_list = (x['totalHrs'] / x['eachSlot'])
#print(totallectures_list)


# Create empty dataframe to save
#new_y = pd.DataFrame(index=range(int(totallectures_list.sum())), columns=list(x))
#j = 0
#for i in range(len(new_y)):
#    if((x.iloc[j]['totalHrs']/x.iloc[j]['eachSlot'])>0):
#        new_y.loc[[i]] = x.iloc[[j]].values
#        x.set_value(j,'totalHrs', x.loc[j]['totalHrs'] - x.loc[j]['eachSlot'])
#    if (x.iloc[j]['totalHrs'] == 0):
#        j = j + 1
#print(new_y)

#new_y.to_csv("newy.csv")

# Create new panel
#timetable1 = pd.Panel(items=10, major_axis=5, minor_axis=10, dtype=int)  # Check if we can do something by dtype = some class here
#print(timetable1)
#timetable1[3][2][4] = 7
#print(timetable1[3])

