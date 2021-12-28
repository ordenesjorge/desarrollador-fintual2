class Stock:

    def __init__(self, name, history):
        self.name = name
        self.history = history
        self.release_date = history['date'].min()

    def price(self, date):
        if date in list(self.history['date']):
            return self.history[self.history['date'] == date]['price'].values[0]
        else:
            print('date not in history of stock')
            # defaults to first value of stock
            return None
