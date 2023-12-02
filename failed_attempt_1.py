import pandas as pd
import random
import numpy as np

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()
print(data)


def table_(data) -> str:
    rows = [len(data)]
    cols = [len(data[:2])]
    new_list = []
    rows[1] = rows.append('robot')
    rows[2] = rows.append('human')
    for i, r in range(rows):
        if data[i] == 'robot':
            new_list[r] = "1"
        else:
            new_list[r] = "0"
        for c in range(cols):
            item = str(data[r][c])
            new_list.append(item)
        print(new_list)


table_(data)
