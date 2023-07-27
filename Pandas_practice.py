import numpy as np
import pandas as pd

mylist = list("abcdefghijklmnopqrstuvwxyz")
myarray = np.arange(26)
mydict = dict(zip(mylist, myarray))

##########################################
# Creates a pandas series from the items #
##########################################

ser1 = pd.Series(mydict)
print(ser1.head())
print("-------------------")

##########################################
# Convert index of series to a dataframe #
##########################################

df = ser1.to_frame().reset_index()
print(df.head())
print("-------------------")

#############################################
# Combine multiple series to make dataframe #
#############################################

ser1 = pd.Series(mylist)
ser2 = pd.Series(myarray)

df = pd.concat([ser1, ser2], axis = 1)
df = pd.DataFrame({"col1": ser1, "col2": ser2})
print(df.head())
print("-------------------")

###############################
# Assign name to series index #
###############################






