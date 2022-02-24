import pandas as pd
ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 9])
ds = ds1 + ds2
print("Adiciona duas Series:")
print(ds)
print("Subtrai duas series:")
ds = ds1 - ds2
print(ds)
print("Multiplica duas Series:")
ds = ds1 * ds2
print(ds)
print("Divide Series1 pela Series2:")
ds = ds1 / ds2
print(ds)
