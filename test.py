import pandas as pd
from datetime import datetime

dict = {'a': [1, 2, 3],
        'b': [13, 124, 231]}
df = pd.DataFrame(dict)
df['datetime'] = datetime.now()

df.to_csv('test.csv')
