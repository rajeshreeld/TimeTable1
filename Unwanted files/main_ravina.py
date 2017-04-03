import dataAccessSQLAlchemy as da
import pandas as pd
import random
import numpy as np

def isSlotAvailable(req_all, timetable_np, c, r_day, r_slot, r_lecnumber, req_id):
    #If slot is of duration 1
    SlotsAvailable = 0
    SlotRequirement=int(req_all.loc[req_id, 'eachSlot'])
    print(SlotRequirement)
    for i in range(SlotRequirement): #Fetching how many lectures do we require to slot
        if(np.isnan(np.sum(timetable_np[int(c), r_day, r_slot+i, r_lecnumber]))):  # Check if that slot is empty, this way of using np.isnan is the fastest way of doing so
            req = req_all.loc[req_all.index == req_id]
            if(req.loc[req_id,'category']=='T'): cat='L'
            else: cat='T'
            req_list= timetable_np[int(c), r_day, r_slot+i, :]
             #Fetch the requirement records of the selected values
            if(not np.isnan(np.sum(req_list))):
                if(cat in req_all.loc[set(req_list), 'category']):   #Allow only if there is another lecture of same type, or no lecture at all
                    SlotsAvailable=SlotsAvailable+1
            else:
                SlotsAvailable = SlotsAvailable + 1
        else:
            break
    if(SlotsAvailable==SlotRequirement):
        return True
    else:
        return False

def initialize_population(p):
    P=None*p
    for i in range(p):
        tt = create_random_timetable(n_classes=14, n_days=5, n_slots=10, n_maxlecsperslot=4, req_all=req_all)
        P[i]=tt
    return P

def find_fitness(h):
    max_penalty=100
    penalty=1*teacher_overlap(h)+ 1*class_batch_overlap(h)
    fitness=penalty-max_penalty
    return fitness

def run_genetic(Fitness, Fitness_Threshold, p, r, m):
    P=initialize_population(p)
    Fitness_P=np.empty(p)
    i=0
    for h in P:
        i=i+1
        Fitness_P[i]=find_fitness(h)
    while(np.max(Fitness_P)<Fitness_Threshold):
        P_s=None*p



def teacher_overlap(timetable):
    teacher_cost = 0
    n_classes, n_days, n_slots, n_maxlecsperslot=timetable.shape
    print timetable.shape
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

def class_batch_overlap(timetable):
    class_cost = 0
    batch_cost = 0
    n_classes, n_days, n_slots, n_maxlecsperslot=timetable.shape
    for cl in range(n_classes):
        for day in range(n_days):
            for slot in range(n_slots):
                class_list = []
                batch_list = []
                slot_array = timetable[cl,day,slot,:]
                for sub_slot in slot_array:
                    if not np.isnan(sub_slot):
                        req = req_all.loc[req_all.index == sub_slot]
                        if (req.iloc[0]['category'] == 'T'):
                            class_list.append(req.iloc[0]['classId'])
                        elif req.iloc[0]['category'] == 'L':
                            batch_list.append(req.iloc[0]['batchId'])

                for class_id in class_list:
                    class_cost = class_cost + class_list.count(class_id)-1

                for batch_id in batch_list:
                    batches_can_overlap = f_batch_can_overlap[f_batch_can_overlap['batchId']==batch_id]
                    batches = batches_can_overlap['batchOverlapId']
                    print(batches)
                    for batch in batch_list:
                        batch_cost = batch_cost + batch_list.count(batch_id) - 1

    #print(batch_cost)
    #print(class_cost)
    return (class_cost + batch_cost)

def create_random_timetable(n_classes, n_days, n_slots, n_maxlecsperslot, req_all):
    timetable_np = np.empty((n_classes, n_days, n_slots, n_maxlecsperslot)) * np.nan
    # print(timetable_np)
    for c in (set(req_all.classId)):  # First take one class
        # print(c)
        # http://stackoverflow.com/questions/17071871/select-rows-from-a-dataframe-based-on-values-in-a-column-in-pandas
        req_forgivenclass = req_all.loc[
            req_all['classId'] == c]  # List all the requirements for that class in req_forgivenclass
        # print(req_forgivenclass)
        # print(set(req_forgivenclass.index))     #These are the indices of the requirements for this class
        for req in set(req_forgivenclass.index):  # Schedule each of these requirements
            notassigned = 1
            while (notassigned == 1):  # Keep on scheduling till not found
                r_day = random.randint(0, n_days - 1)
                r_slot = random.randint(0, n_slots - 1)
                r_lecnumber = random.randint(0, n_maxlecsperslot - 1)
                if (isSlotAvailable(req_all, timetable_np, c, r_day, r_slot, r_lecnumber, req)):
                    timetable_np[int(c), r_day, r_slot, r_lecnumber] = req
                    notassigned = 0
    return timetable_np




print("Welcome");

f_subject_subjectClassTeacher = da.execquery('select s.subjectId, subjectShortName, totalHrs, eachSlot, c.classId, teacherId from subject s, subjectClassTeacher c where s.subjectId = c.subjectId;')
f_subject_subjectClassTeacher.insert(5,'batchId','-')
f_subject_subjectClassTeacher.insert(6,'category','T') #T for theory
f_subject_subjectBatchTeacher = da.execquery('select s.subjectId, subjectShortName, totalHrs, eachSlot, sbt.batchId, bc.classId, teacherId from subject s, subjectBatchTeacher sbt, batchClass bc where s.subjectId = sbt.subjectId AND sbt.batchId = bc.batchId;')
f_subject_subjectBatchTeacher.insert(6,'category','L') #L for Lab
f_subjectBatchClassTeacher = pd.concat([f_subject_subjectClassTeacher, f_subject_subjectBatchTeacher])
f_batch_can_overlap = da.execquery('select batchId, batchOverlapId from batchCanOverlap;')
print(f_batch_can_overlap)
x = f_subjectBatchClassTeacher
x = x.reset_index()

totallectures_list = (x['totalHrs'] / x['eachSlot'])


# Create empty dataframe to save all the requirements
req_all = pd.DataFrame(index=range(int(totallectures_list.sum())), columns=list(x))
j = 0
for i in range(len(req_all)):
    if((x.iloc[j]['totalHrs']/x.iloc[j]['eachSlot'])>0):
        req_all.loc[[i]] = x.iloc[[j]].values
        x.set_value(j,'totalHrs', x.loc[j]['totalHrs'] - x.loc[j]['eachSlot'])
    if (x.iloc[j]['totalHrs'] == 0):
        j = j + 1
#print(req_all)
#These were attempts to convert float values in reqall to int
#req_all[['classId','eachSlot', 'subjectId', 'totalHrs']] = req_all[['classId','eachSlot', 'subjectId', 'totalHrs']].apply(pd.to_numeric)
#req_all=req_all.apply(pd.to_numeric, errors='ignore')

#These values need to be calculated from the database
tt1=create_random_timetable(n_classes=14, n_days=5, n_slots=10, n_maxlecsperslot=4, req_all=req_all)

#teacher_cost = teacher_overlap(tt1)
#print("Teacher cost:")
#print(teacher_cost);

#cb_cost = class_batch_overlap(tt1)
#print("Class cost:")
#print(cb_cost);


finalTT=runGenetic(Fitness, Fitness_threshold, p=20, r, m) #p=population size, r=crossover fraction, m=mutation rate