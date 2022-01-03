class Stock:

    # history must be a pandas dataframe with columns name,date,price
    def __init__(self, name, history):
        self.name = name
        self.history = history
        self.release_date = history['date'].min()

    # date must be datetime64
    def price(self, date):
        if date in list(self.history['date']):
            return self.history[self.history['date'] == date]['price'].values[0]
        else:
            print('date not in history of stock')
            return None
