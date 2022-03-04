import pandas as pd
import numpy as np
s1 = pd.Series(['100', '200', 'python', '300.10', '400'])
print('Data Series Original')
print(s1)
print('Series para Array')
a = np.array(s1.values.tolist())
print(a)

