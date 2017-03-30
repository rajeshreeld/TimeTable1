import dataAccessSQLAlchemy as da
import pandas as pd
import numpy
import random
import numpy as np



f_room = da.initialize('room');
lab_group = []
theory_group = []
for r in f_room:
    print(r.iloc['roomId']);
    #if (r['roomCount'] <= 25):
     #   lab_group.append(r.roomId);
    #else:
     #   theory_group.append(r.roomId);


print(lab_group);
print(theory_group);