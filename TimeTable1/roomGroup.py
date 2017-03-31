import dataAccessSQLAlchemy as da
import pandas as pd
import numpy
import random
import numpy as np



def get_room_groups(lab_group, theory_group):
    "Forms 2 groups of rooms. lab_group contains rooms with roomCount < 25, all others in theory_group"

    f_room = da.initialize('room');

    for i in range(len(f_room)):
        if (f_room.iloc[i]['roomCount'] > 25):
            theory_group.append(f_room.iloc[i]['roomId']);
        else:
            lab_group.append(f_room.iloc[i]['roomId']);



lab_group = []
theory_group = []

get_room_groups(lab_group, theory_group);

print(theory_group, len(theory_group));
print(lab_group, len(lab_group));
