import pandas as pd
import random
import numpy as np

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()
print(data)


def lst1and2(data):
    lst1 = 'Robot'
    lst2 = 'Human'
    for i in data:
        if i == 'robot':
            lst1 = lst1.append({1})
        else:
            lst1 = lst1.append({0})
        return (lst1)
    for i in data:
        if i == 'human':
            lst2 = lst2.append({1})
        else:
            lst2 = lst2.append({0})
        return (lst2)
    res = pd.DataFrame({'Robot': lst1, 'Human': lst2})
    res.set_index([pd.Series([1, 2, 3, 4]), 'Robot', 'Human'])
    print(res)


lst1and2(data)
