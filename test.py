import pandas as pd

dict = {'a': [1, 2, 3],
        'b': [13, 124, 231]}
df = pd.DataFrame(dict)

df.to_csv('test.csv')
