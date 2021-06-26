import pandas as pd

dic ={"first": [1,2,3], "key": 5, "door": "window"}
series_dict = pd.Series(dic)
print(series_dict)

## index
# print(dic[0]) this is key error
print(series_dict[1])

# series is mutable
series_dict["door"] = 10

## more than 1 index
print("------------------here ---------------")
print(series_dict[[0,1]])
print("------------------loc------------------")
print(series_dict.loc["first": "door"])
print("------------------iloc------------------")
print(series_dict.iloc[0:2])

## drop elements
print("-------------------drop------------------")
print(series_dict.drop(labels = "first"))

# math
series1 = pd.Series([1,5,2])
series2 = pd.Series([10,3,5])

print(series1.add(series2))
# print(series1.sub(series2))
print(series1 + series2)