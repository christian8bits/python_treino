import pandas as pd
s = pd.Series(['100', '200', 'python', '300.12', '400'])
print("Data Series Original:")
print(s)
print("\nData Series depois da adição de dados:")
new_s = s.append(pd.Series(['500', 'php']))
print(new_s)
