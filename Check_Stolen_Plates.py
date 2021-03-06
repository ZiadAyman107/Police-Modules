import pandas as pd
import numpy as np
Plates = pd.read_excel("Stolen Car Plates DataBase/Stolen Plates.xlsx", header=None, index_col=False)
Stolen_Plates = []
for i in range(len(Plates)):
    x = np.flip(np.array(Plates.loc[i, :]).astype(str), 0)
    Stolen_Plates.append(x)

def Compare_Plates(Current_Plate):
    Current_Plate = np.array(Current_Plate)
    for i in range(len(Plates)):
        if len(Current_Plate) != len(Stolen_Plates[i]):
            continue
        comparison = Current_Plate == Stolen_Plates[i]
        equal_arrays = comparison.all()
        return equal_arrays

    return False


