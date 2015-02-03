from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "C:\Users\Kyle\Documents\NSOE_semester_4\Building EoC\project"
csv_file = "Utility_Summary.csv"
ele_file = "elec.csv"
steam_file = "steam.csv"
chill_file = "chilledwater.csv"

# importing data
dfelec = pd.read_csv(os.path.join(main_dir, ele_file))
dfsteam = pd.read_csv(os.path.join(main_dir, steam_file))
dfchill = pd.read_csv(os.path.join(main_dir, chill_file))

del dfelec['Month']
del dfsteam['Month']
del dfchill['Month']


#totals (In Series)

etotal = sum(dfelec)
cwtotal = sum(dfchill)
stotal = sum(dfsteam)

