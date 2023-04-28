import random
import numpy as np
import pandas as pd


my_list = []
for i in range(10):
    my_list.append(random.randint(0,100))

Dane1 = pd.DataFrame(my_list)

my_dict = {
    'a': [3,6,7],
    'b': [4,2,9],
    'c': [6,3,3],
    'd': [1,2,8]
}

Dane2 = pd.DataFrame(my_dict)

my_array = np.arange(12).reshape(4,3)
for i in range(4):
    for j in range(3):
        my_array[i][j] = random.randint(0,9)

Dane3 = pd.DataFrame(my_array)

my_series = pd.Series([5,2,5,85,12],
                      index=['a','b','c','d','e'])

Dane4 = pd.DataFrame(my_series)

print(Dane1, "\n", Dane2, "\n", Dane3, "\n", Dane4)

print(Dane1.values.tolist())
print(Dane2.to_dict("dict"))
print(pd.DataFrame(Dane3).to_numpy())
print(Dane4.to_dict("series"))
