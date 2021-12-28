import numpy as np
import pandas as pd

# stocks as (name, year, initial_price)
stocks = [
    ('AAPL', 1980, 22),
    ('NVDA', 1999, 12),
    ('TSLA', 2010, 17)
    ]

data = []

for stock in stocks:

    dti = list(
        pd.date_range(
            start=str(stock[1]) + '-01-01',
            end='2022-01-01',
            freq='D'
        )
    )

    n_rows = len(dti)

    stock_name_col = [stock[0]] * n_rows

    prices = list(
        np.random.default_rng().uniform(
            low=stock[2], 
            high=stock[2]*(1+0.01*n_rows), 
            size=n_rows
        )
    )

    data.append(
        pd.DataFrame.from_records(
            zip(stock_name_col,dti,prices),
            columns=['name','date','price']
        )
    )

data = pd.concat(data)

data.to_csv('data.csv', index=False)