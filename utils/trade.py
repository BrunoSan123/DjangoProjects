import pandas as pd
import pandas_datareader as pdr

lt = ['AZUL', 'MSFT', 'JPM', 'GOL', 'F']

db = pd.DataFrame()

for i in lt:
    df = pdr.DataReader(i, 'yahoo', '2020-4-13', '2020-4-13')
    df['ATIVO'] = i
    print(df.head(), df.tail())
    db = pd.concat([db, df], sort=True)

df = df.set_index('Date')

print(df.heat())
