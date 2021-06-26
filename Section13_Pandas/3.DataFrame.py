import pandas as pd
import numpy as np

## Dict to Frame

# the value should be the same size as other
di = {"tweet": [1,2,3], "user": ["phat", "khanh", "man"], "verified": [True, False, True]}
df_di = pd.DataFrame(di)
print(df_di)

# if we use SERIES value can be different size
di_series = {"tweet": pd.Series([1,2,3]), "user": pd.Series(["phat", "khanh", "man"]), "verified": pd.Series([True, False, True])}
df_di_series = pd.DataFrame(di_series)
print(df_di_series)

# ndarrays/ lists to Frame
arr = pd.Series([1,2,3])  # this can be list, dict
df_arr = pd.DataFrame(arr, columns=["list"])
print(df_arr)

## From a list of dicts to Frame
list_dict = [{"a":2, "c": 4.5}, {"c":4, "b":1}]
df_list_dict = pd.DataFrame(list_dict)
print(df_list_dict)

## 2-D numpy.ndarray
np_arr = 4.5*np.ones((3,3))
df_np = pd.DataFrame(np_arr, columns=[1,2,3])
print(df_np)

## Another DataFrame: to store the output
df_np2 = pd.DataFrame(df_np)
print(df_np2)

## from csv file