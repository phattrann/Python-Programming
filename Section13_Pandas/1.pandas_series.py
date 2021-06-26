import pandas as pd
import numpy as np

## From ndarray
arr = np.array([1,2,3,7])
series = pd.Series(arr)
print(series)
print("size", series.size)

## From a list
series_list = pd.Series([1,10,3])
print(series_list)

## From dict
di = {"first": 3 , "second": 2.1, "third": 2}
seriesdict = pd.Series(di)
# seriesdict = pd.Series(data=di, index=['fst', 'sc', 'thr'])
print("From dict: ",seriesdict)
print(seriesdict["first"])

## From Scalar value
scalar_value = 10
series_scalar = pd.Series(scalar_value, index = [0,1,2,3,4,])
print("Scalar: ", series_scalar)

## numpy-like
print(seriesdict.dtype)
np_arr = series_scalar.to_numpy()
print("np-like: ",np_arr)

## dict-like
print("dict-like: ",series_scalar.get(3))

## shape
print("shape: ",series_scalar.shape)

## ndim
print("ndim: ",series_scalar.ndim)

## size
print("size: ",series_scalar.size)