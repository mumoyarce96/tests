import pandas as pd
from datetime import datetime

url = 'https://raw.githubusercontent.com/mumoyarce96/tests/main/test.csv'
prev_df = pd.read_csv(url, index_col = False).drop('Unnamed: 0', axis = 1)

dict = {'a': [1, 2, 3],
        'b': [13, 124, 231]}

df = pd.DataFrame(dict)
df['datetime'] = datetime.now()
df = pd.concat([prev_df, df]).reset_index(drop = True)
df.to_csv('test.csv', index = False)
