import pandas as pd
from datetime import datetime

url = (r'https://raw.githubusercontent.com/mumoyarce96/sofascore_API_call/main/test.csv?token=GHSAT0AAAAAACQTQBYWACC4SVVWXZ3JRSWUZQQS64Q')
prev_df = pd.read_csv(url)

dict = {'a': [1, 2, 3],
        'b': [13, 124, 231]}

df = pd.DataFrame(dict)
df['datetime'] = datetime.now()
df = pd.concat([prev_df, df])
df.to_csv('test.csv')
